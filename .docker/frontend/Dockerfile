ARG NODE_VERSION

FROM node:${NODE_VERSION}-alpine AS base
WORKDIR /home/node/app
RUN yarn global add @quasar/cli
COPY frontend .

FROM base AS build-stage
RUN yarn install
RUN yarn quasar build

FROM base AS development
CMD ["/bin/sh", "-c", "yarn install && yarn quasar dev"]

FROM nginx:alpine AS production
COPY --from=build-stage /home/node/app/dist/spa /usr/share/nginx/html
COPY .docker/frontend/default.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
