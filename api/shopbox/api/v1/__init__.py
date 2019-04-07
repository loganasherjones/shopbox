# -*- coding: utf-8 -*-
from fastapi import APIRouter

from shopbox.api.v1 import project

api_v1_router = APIRouter()
api_v1_router.include_router(project.router)
