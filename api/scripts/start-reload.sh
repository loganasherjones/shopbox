#!/usr/bin/env sh
set -e

if [ -d "/app" ]; then
    DEFAULT_APP_DIR="/app"
else
    SCRIPT=$(readlink -f "$0")
    SCRIPTPATH=$(dirname "$SCRIPT")
    DEFAULT_APP_DIR=$(dirname "$SCRIPTPATH")
fi

APP_MODULE="shopbox.main:app"
APP_DIR=${APP_DIR:-$DEFAULT_APP_DIR}
HOST=${HOST:-0.0.0.0}
PORT=${PORT:-8080}
LOG_LEVEL=${LOG_LEVEL:-info}

# If there's a prestart.sh script in the APPDIR, run it before starting.
PRE_START_PATH="${APP_DIR}/prestart.sh"
echo "Checking for script in $PRE_START_PATH"
if [ -f $PRE_START_PATH ]; then
    echo "Running script $PRE_START_PATH"
    . "$PRE_START_PATH"
else
    echo "There is no script $PRE_START_PATH"
fi

echo "$APP_MODULE"
echo "$APP_DIR"
# Start Uvicorn with live reload
exec uvicorn --reload --host $HOST --port $PORT --log-level $LOG_LEVEL "$APP_MODULE"