# -*- coding: utf-8 -*-
from sanic.response import json
from sanic import Blueprint


bp = Blueprint("project", url_prefix="/projects")


@bp.route("/")
async def index(request):
    return json({"projects": "TODO"})
