#!/bin/sh
flask db migrate
flask db upgrade
if [ "$FLASK_ENV" = "development" ]
then
    flask run --host=0.0.0.0
else
    gunicorn wsgi:app -w 4 -b 0.0.0.0:80 --capture-output --log-level debug
fi
