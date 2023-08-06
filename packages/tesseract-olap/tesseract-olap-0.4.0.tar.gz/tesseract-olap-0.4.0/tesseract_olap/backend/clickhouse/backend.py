import logging
from contextlib import asynccontextmanager
from typing import AsyncIterator, Union

from aioch import Client
from clickhouse_driver import errors

from tesseract_olap.backend import Backend
from tesseract_olap.backend.exceptions import UpstreamInternalError
from tesseract_olap.common import AnyTuple
from tesseract_olap.query import DataQuery, MembersQuery
from tesseract_olap.query.exceptions import InvalidQuery
from tesseract_olap.schema import Schema

from .sqlbuild import dataquery_sql, membersquery_sql

logger = logging.getLogger("tesseract_olap.backend.clickhouse")


class ClickhouseBackend(Backend):
    """Clickhouse Backend class

    This is the main implementation for Clickhouse of the core :class:`Backend`
    class.

    Must be initialized with a connection string with the parameters for the
    Clickhouse database. Then must be connected before used to execute queries,
    and must be closed after finishing use.
    """

    connection_string: str

    def __init__(self, connection_string: str) -> None:
        self.connection_string = connection_string

    def __repr__(self) -> str:
        return f"ClickhouseBackend('{self.connection_string}')"

    @asynccontextmanager
    async def _acquire(self):
        client = Client.from_url(self.connection_string)
        try:
            yield client
        except errors.ServerException as exc:
            raise UpstreamInternalError(str(exc)) from None
        finally:
            await client.disconnect()

    async def connect(self, **kwargs):
        pass

    def close(self):
        pass

    async def wait_closed(self):
        pass

    async def execute(
        self,
        query: Union["DataQuery", "MembersQuery"],
        **kwargs
    ) -> AsyncIterator[AnyTuple]:
        """
        Processes the requests in a :class:`DataQuery` or :class:`MembersQuery`
        instance, sends the query to the database, and returns an `AsyncIterator`
        to access the rows.
        Each iteration yields a tuple of the same length, where the first tuple
        defines the column names, and the subsequents are rows with the data in
        the same order as each column.
        """
        logger.debug("Execute query", extra={"query": query})

        if isinstance(query, MembersQuery):
            sql_builder, sql_params = membersquery_sql(query)
        elif isinstance(query, DataQuery):
            sql_builder, sql_params = dataquery_sql(query)
        else:
            raise InvalidQuery(
                "ClickhouseBackend only supports DataQuery and MembersQuery instances"
            )

        async with self._acquire() as cursor:
            result = await cursor.execute_iter(query=sql_builder.get_sql(),
                                               params=sql_params,
                                               settings={"max_block_size": 5000},
                                               with_column_types=True)
            async for row in result:
                yield row

    async def ping(self) -> bool:
        """Checks if the current connection is working correctly."""
        async with self._acquire() as cursor:
            result = await cursor.execute("SELECT 1")
            return result == [(1,)]

    async def validate_schema(self, schema: "Schema") -> None:
        """Checks all the tables and columns referenced in the schema exist in
        the backend.
        """
        # logger.debug("Schema %s", schema)
        # TODO: implement
        for cube in schema.cube_map.values():
            pass
        return None
