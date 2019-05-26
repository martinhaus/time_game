#!/bin/sh

export FLASK_ENV=development
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
env FLASK_APP=app.py flask run 