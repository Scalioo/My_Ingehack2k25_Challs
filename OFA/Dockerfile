FROM python:3-alpine

RUN apk update && \
    apk add socat && pip install pycryptodome

COPY ./dist /dist

WORKDIR /dist

RUN chmod +x entrypoint.sh server.py 

EXPOSE 2000

ENTRYPOINT ["./entrypoint.sh"]