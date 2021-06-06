# FROM python:3.7
FROM python:3.9-alpine

RUN apk update \
    && apk add --no-cache build-base gcc libc-dev python3-dev mariadb-dev

WORKDIR /usr/src/server
ADD requirements.txt .
RUN pip install --upgrade pip \
    && pip install --trusted-host pypi.python.org -r requirements.txt

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
