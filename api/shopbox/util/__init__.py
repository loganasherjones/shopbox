from os import environ

from gino.ext.sanic import Gino
from sanic_limiter import Limiter, get_remote_address

from sanic import Sanic


def sanic_config_manager(app: Sanic, prefix: str = "SANIC_"):
    app.config.DB_DATABASE = "shopbox"
    for variable, value in environ.items():
        if variable.startswith(prefix):
            _, key = variable.split(prefix, 1)
            app.config[key] = value


def setup_database_creation_listener(app: Sanic, database: Gino):
    database.init_app(app)

    @app.listener("after_server_start")
    async def setup_database(app: Sanic, loop):
        await database.gino.create_all()


def setup_rate_limiter(app: Sanic):
    limiter = Limiter(
        app,
        global_limits=["1000/hour", "100/second"],
        key_func=get_remote_address,
        strategy="moving-window",
        storage_uri="memory://",
    )

    return limiter
