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
Limit Node

This is a SQL Query Execution Plan Node.

This Node returns up to a specified number of tuples.
"""
from typing import Iterable

from pyarrow import Table, concat_tables

from opteryx.exceptions import SqlError
from opteryx.models import QueryProperties, QueryStatistics
from opteryx.operators import BasePlanNode


class LimitNode(BasePlanNode):
    def __init__(
        self, properties: QueryProperties, statistics: QueryStatistics, **config
    ):
        super().__init__(properties=properties, statistics=statistics)
        self._limit = config.get("limit")

    @property
    def name(self):  # pragma: no cover
        return "Limitation"

    @property
    def config(self):  # pragma: no cover
        return str(self._limit)

    def execute(self) -> Iterable:

        if len(self._producers) != 1:
            raise SqlError(f"{self.name} on expects a single producer")

        data_pages = self._producers[0]  # type:ignore
        if isinstance(data_pages, Table):
            data_pages = (data_pages,)

        result_set = []
        row_count = 0
        page = None

        for page in data_pages.execute():
            if page.num_rows > 0:
                row_count += page.num_rows
                result_set.append(page)
                if row_count > self._limit:  # type:ignore
                    break

        if len(result_set) == 0:
            yield page
        else:
            yield concat_tables(result_set, promote=True).slice(
                offset=0, length=self._limit
            )
