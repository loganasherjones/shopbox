# -*- coding: utf-8 -*-
from shopbox.dao import ProjectDAO

from sanic import Blueprint
from sanic.response import json


bp = Blueprint(name="project", url_prefix="/projects")


@bp.route("/")
async def get_projects(request):
    projects = await ProjectDAO.get_projects()
    return json([p.to_dict() for p in projects])


@bp.route("/<project_name>")
async def get_project(request, project_name):
    project = await ProjectDAO.get_project(project_name)
    return json(project.to_dict())
