# -*- coding: utf-8 -*-

from fastapi import FastAPI
from starlette.requests import Request

from shopbox.core import config
from shopbox.api.v1 import api_v1_router
from shopbox.db.session import Session


app = FastAPI(title=config.PROJECT_NAME, openapi_url="/api/v1/openapi.json")

# TODO: Setup CORS

app.include_router(api_v1_router, prefix=config.API_V1_STR)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.db = Session()
    response = await call_next(request)
    request.state.db.close()
    return response
