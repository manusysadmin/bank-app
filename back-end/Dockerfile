FROM python:3.7

COPY requirements.txt /backend/
WORKDIR /backend/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip3 install -r requirements.txt
COPY . /backend/
