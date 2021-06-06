FROM node:lts-alpine

RUN apk update && \
    npm install -g @vue/cli

WORKDIR /app/vue-app

#shファイルをコンテナにコピー
COPY ./scripts/docker.start.sh /scripts/start.sh

EXPOSE 8080

# #shフォルダの権限追加（全員実行可）
RUN chmod +x /scripts/*

# # #初期実行
ENTRYPOINT [ "/scripts/start.sh" ]