FROM node:16 as build

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . ./
RUN npm run build

FROM node:16-slim

WORKDIR /app

COPY --from=build /app/build ./build
COPY --from=build /app/public ./public

RUN yarn global add serve

ENV API_URL=api

EXPOSE 80

CMD ["serve", "-s", "build", "-l", "80"]
