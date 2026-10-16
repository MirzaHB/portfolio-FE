FROM node:22-alpine AS build

WORKDIR /app

COPY package*.json ./
RUN npm ci

ARG VITE_API_BASE_URL=/api
ARG VITE_MSAL_CLIENT_ID
ARG VITE_MSAL_TENANT_ID
ARG VITE_MSAL_REDIRECT_URI

COPY . .
RUN npm run build

FROM nginx:alpine AS runtime

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
