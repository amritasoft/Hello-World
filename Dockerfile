from python:3.8.3-alpine3.12

workdir /usr/app



copy ./requirements.txt .

copy ./test_1/ ./test_2/ ./

run pip install -r requirements.txt
RUN apk add curl jq


cmd ["sh", "healthcheck.sh"]