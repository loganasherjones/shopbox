# -*- coding: utf-8 -*-
import urllib.parse

from shopbox.models.pagination import Links
from shopbox.models.project import PaginatedProject
from shopbox.db_models.project import Project


def get_multi(db_session, base_url, *, skip=0, limit=100) -> PaginatedProject:
    limit = min(limit, 1000)
    count = db_session.query(Project).count()
    projects = db_session.query(Project).offset(skip).limit(limit).all()
    current_query = urllib.parse.urlencode({"skip": skip, "limit": limit})
    if count > skip + limit:
        next_query = urllib.parse.urlencode({"skip": skip + limit, "limit": limit})
        next_url = f"{base_url}?{next_query}"
    else:
        next_url = None

    links = Links(
        base=base_url, context="", next=next_url, current=f"{base_url}?{current_query}"
    )
    new_projects = [p.__dict__ for p in projects]
    result = PaginatedProject(
        results=new_projects,
        limit=limit,
        total_count=count,
        page_count=min(limit, count - skip),
        start=skip,
        links=links,
    )
    return result
