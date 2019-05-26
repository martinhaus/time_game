FROM python:latest

ENV DATABASE_URL postgresql://postgres:postgres@db:5432/time_game

WORKDIR /app

COPY . .
RUN rm -rf migrations 

RUN pip install -r requirements.txt

ENV FLASK_ENV development
ENV FLASK_APP app.py

ENTRYPOINT ./run.sh