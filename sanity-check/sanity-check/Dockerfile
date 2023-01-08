FROM alpine:latest

RUN apk update && \
    apk add socat

COPY ./challenge/entrypoint.sh /

RUN chmod 555 /entrypoint.sh 

EXPOSE 1337

ENTRYPOINT ["/entrypoint.sh"]