from functools import partial

from fastapi import FastAPI, Request, Response

from dropland.blocks import async_resource_session
from dropland.data.context import with_context


def add_middleware(
        app: FastAPI, begin_sql_tx: bool = True, autocommit: bool = True):
    @app.middleware('http')
    async def resource_session_middleware(request: Request, call_next) -> Response:
        with with_context():
            return await async_resource_session(
                partial(call_next, request), begin_tx=begin_sql_tx, autocommit=autocommit
            )
