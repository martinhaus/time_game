#!/bin/sh

export FLASK_ENV=development
python3 manage.py db init
python3 manage.py db migrate
python3 manage.py db upgrade
env FLASK_APP=app.py flask run 
