# -*- coding: utf-8 -*-
from pydantic import BaseModel


class Links(BaseModel):
    base: str = None
    context: str = None
    next: str = None
    current: str = None


class PaginationBase(BaseModel):
    limit: int = None
    total_count: int = None
    page_count: int = None
    start: int = None
    links: Links = None
