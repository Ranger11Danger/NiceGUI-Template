FROM alpine:latest

RUN apk add --update --no-cache python3
RUN apk add --update --no-cache py3-pip
RUN apk add make automake gcc g++ subversion python3-dev
RUN pip3 install nicegui
RUN pip3 install itsdangerous
RUN pip3 install requests


WORKDIR /app
ENTRYPOINT [ "python3", "startup.py" ]