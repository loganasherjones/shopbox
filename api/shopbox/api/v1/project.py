# -*- coding: utf-8 -*-
from fastapi import Depends, APIRouter
from starlette.requests import Request
from sqlalchemy.orm import Session

from shopbox import crud
from shopbox.models.project import PaginatedProject
from shopbox.api.utils.db import get_db

router = APIRouter()


@router.get(
    "/projects",
    tags=["projects"],
    response_model=PaginatedProject,
    name="read_projects",
)
def read_projects(
    request: Request, db: Session = Depends(get_db), skip: int = 0, limit: int = 100
):
    return crud.project.get_multi(
        db, request.url_for("read_projects"), skip=skip, limit=limit
    )
