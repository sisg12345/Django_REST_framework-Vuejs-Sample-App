FROM node:18-alpine

WORKDIR /usr/src

ENV HOST 0.0.0.0

EXPOSE 8080

RUN apk update && npm install -g npm @vue/cli && yarn install

CMD ["/bin/sh"]