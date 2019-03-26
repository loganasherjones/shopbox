from sanic_openapi import doc, openapi_blueprint, swagger_blueprint
from shopbox.blueprint.health import health
from shopbox.blueprint.project import bp as project_bp
from shopbox.model import db
from shopbox.util import setup_database_creation_listener, setup_rate_limiter

from sanic import Sanic
from sanic.response import json


app = Sanic(__name__)

limiter = setup_rate_limiter(app)


app.blueprint(openapi_blueprint)
app.blueprint(swagger_blueprint)

app.blueprint(health)

app.blueprint(project_bp)
setup_database_creation_listener(app, db)


@app.route("/")
async def default(request):
    return json({"message": "hello Sanic!"})
