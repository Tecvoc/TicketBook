FROM python:3.8-slim

RUN mkdir /home/work


WORKDIR /home/work

COPY requirements.txt .
RUN pip install -r requirements.txt && rm -f requirements.txt

COPY fixtures/movie_app_data.json .
COPY src .
