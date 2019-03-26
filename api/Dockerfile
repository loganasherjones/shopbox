FROM python:3.6-slim
MAINTAINER Logan Asher Jones


# Start Installing the Basic Dependencies
RUN pip install --upgrade pip
RUN pip install gunicorn

RUN mkdir -p /sanic/config
RUN mkdir -p /sanic/shopbox

COPY config/* /sanic/config/
COPY shopbox/ /sanic/shopbox/
COPY requirements.txt /sanic
COPY run.py /sanic/run.py
COPY .env /sanic/.env

WORKDIR /sanic
RUN find . -type f

ENV SHOPBOX_SERVER_PORT 8000
ENV SHOPBOX_SERVER_HOST 0.0.0.0

EXPOSE 8000


ENTRYPOINT ["gunicorn", "run:app", "--config", "/sanic/config/gunicorn.conf", "--log-config", "/sanic/config/logging.conf", "-b", "0.0.0.0:8000", "--worker-class",  "sanic.worker.GunicornWorker"]

