FROM python:3.9-slim-buster

WORKDIR /usr/src

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get clean
RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt
