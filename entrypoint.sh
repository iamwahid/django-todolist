#!/bin/bash

# python3 manage.py migrate activity
# python3 manage.py migrate todo

mysql -h $MYSQL_HOST -u $MYSQL_USER -p$MYSQL_PASSWORD $MYSQL_DBNAME < db.sql

# python3 manage.py runserver 0.0.0.0:3030
uvicorn api.asgi:application --workers 10 --host 0.0.0.0 --port 3030