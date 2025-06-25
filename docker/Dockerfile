FROM python:3.12.3-alpine3.20

WORKDIR /src

COPY ./docker/.env .

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY ./docker/init.sh .
RUN chmod +x init.sh