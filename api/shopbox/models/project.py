# -*- coding: utf-8 -*-
from typing import List, Optional
from .pagination import PaginationBase
from pydantic import BaseModel


class ProjectBase(BaseModel):
    name: str = None
    display_name: str = None
    short_description: str = None
    long_description: str = None


class ProjectBaseInDB(ProjectBase):
    id: int = None


class Project(ProjectBaseInDB):
    pass


class PaginatedProject(PaginationBase):
    results: List[ProjectBase] = None
