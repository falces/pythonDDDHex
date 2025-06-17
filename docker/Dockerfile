FROM python:3.12.3-alpine3.20

WORKDIR /src

COPY .env .env

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt