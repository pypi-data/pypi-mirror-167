# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Left Join Node

This is a SQL Query Execution Plan Node.

This performs a LEFT (OUTER) JOIN
"""
from typing import Iterable

import pyarrow

from opteryx.exceptions import SqlError
from opteryx.models import Columns, QueryProperties, QueryStatistics
from opteryx.operators import BasePlanNode
from opteryx.utils import arrow

OUTER_JOINS = {
    "FullOuter": "Full Outer",
    "LeftOuter": "Left Outer",
    "RightOuter": "Right Outer",
}


class OuterJoinNode(BasePlanNode):
    def __init__(
        self, properties: QueryProperties, statistics: QueryStatistics, **config
    ):
        super().__init__(properties=properties, statistics=statistics)
        self._join_type = OUTER_JOINS[config.get("join_type")]
        self._on = config.get("join_on")
        self._using = config.get("join_using")

        if self._on is None and self._using is None:
            raise SqlError("Missing JOIN 'on' condition")

    @property
    def name(self):  # pragma: no cover
        return f"{self._join_type} Join"

    @property
    def config(self):  # pragma: no cover
        return ""

    def execute(self) -> Iterable:

        if len(self._producers) != 2:
            raise SqlError(f"{self.name} expects two producers")

        left_node = self._producers[0]  # type:ignore
        right_node = self._producers[1]  # type:ignore

        right_table = pyarrow.concat_tables(right_node.execute(), promote=True)

        right_columns = Columns(right_table)
        left_columns = None

        for page in arrow.consolidate_pages(left_node.execute(), self._statistics):

            if left_columns is None:
                left_columns = Columns(page)
                try:
                    right_join_column = right_columns.get_column_from_alias(
                        self._on.right.value, only_one=True
                    )
                    left_join_column = left_columns.get_column_from_alias(
                        self._on.left.value, only_one=True
                    )
                except SqlError:
                    # the ON condition may not always be in the order of the tables
                    # we purposefully reference the columns incorrectly
                    right_join_column = right_columns.get_column_from_alias(
                        self._on.left.value, only_one=True
                    )
                    left_join_column = left_columns.get_column_from_alias(
                        self._on.right.value, only_one=True
                    )

                # ensure the types are compatible for joining by coercing numerics
                right_table = arrow.coerce_column(right_table, right_join_column)

            new_metadata = right_columns + left_columns

            page = arrow.coerce_column(page, left_join_column)

            # do the join
            new_page = page.join(
                right_table,
                keys=[left_join_column],
                right_keys=[right_join_column],
                join_type=self._join_type.lower(),
                coalesce_keys=False,
            )
            # update the metadata
            new_page = new_metadata.apply(new_page)
            yield new_page
