FROM nginx:latest
LABEL maintainer="orcahmlee@gmail.com"


COPY nginx.conf /etc/nginx/nginx.conf
COPY docker-nginx-dj3.conf /etc/nginx/sites-available/

RUN mkdir -p /etc/nginx/sites-enabled/ && \
    ln -s /etc/nginx/sites-available/docker-nginx-dj3.conf /etc/nginx/sites-enabled/

CMD ["nginx", "-g", "daemon off;"]
