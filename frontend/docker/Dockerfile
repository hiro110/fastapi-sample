FROM node:lts-alpine

RUN apk update && \
    npm install -g @vue/cli

WORKDIR /app/vue-app

COPY ./scripts/docker.start.sh /scripts/start.sh

EXPOSE 8080

RUN chmod +x /scripts/*

ENTRYPOINT [ "/scripts/start.sh" ]