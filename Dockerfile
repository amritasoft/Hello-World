from python:3.8.3-alpine3.12

workdir /usr/app

ADD requirements.txt /usr/app/requirements.txt

RUN apk add curl jq

RUN pip install -r requirements.txt



copy . .

ENTRYPOINT sh healthcheck.sh

