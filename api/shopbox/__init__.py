# -*- coding: utf-8 -*-
import logging
from sanic import Sanic
from shopbox.blueprints import api

app = None
logger = None


def setup_logging(config):
    logging.basicConfig(**config["log"])


def setup_app(config):
    global app, logger
    logger = logging.getLogger(__name__)
    app = Sanic(name="shopbox_api")
    app.blueprint(api)


def run(config):
    host = config["web"]["host"]
    port = config["web"]["port"]
    logger.info("Running sanic on %s:%d", host, port)
    app.run(host, port, config["web"]["debug"], access_log=False)


def stop():
    app.stop()
