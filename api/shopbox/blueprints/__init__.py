# -*- coding: utf-8 -*-
from sanic import Blueprint

from shopbox.blueprints.project import bp as project_bp

api = Blueprint.group(project_bp, url_prefix="/api/v1")
