# -*- coding: utf-8 -*-
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.requests import Request

from shopbox import crud
from shopbox.api.utils.db import get_db
from shopbox.models.project import PaginatedProject

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
