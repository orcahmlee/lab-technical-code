FROM python:3.7
LABEL maintainer="orcahmlee@gmail.com"


WORKDIR /web
COPY . /web/

RUN pip install -r requirements.txt

WORKDIR /web/dj3

VOLUME /web
EXPOSE 8000

ENTRYPOINT [ "/bin/bash", "docker-entrypoint.sh" ]
CMD python manage.py runserver 0.0.0.0:8000
