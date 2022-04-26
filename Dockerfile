# pull official base image
FROM python:3.8.11-slim

# set work directory
WORKDIR /usr/src/demo_drf_api

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get -y upgrade && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    make libpq-dev gcc python3-dev postgresql-client \
    libffi-dev zlib1g-dev libjpeg-dev \
    && apt-get -y clean && apt-get -y autoremove


RUN pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

# copy project
COPY . .
