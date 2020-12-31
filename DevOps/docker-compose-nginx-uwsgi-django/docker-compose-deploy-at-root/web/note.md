# only django

```
docker build -t andrew/dj3 .

docker run --rm -it -p 8000:8000 andrew/dj3

docker run --rm -it -p 8000:8000 -v $(PWD):/app andrew/dj3

docker run --rm -it -p 8003:8003 -v $(PWD):/app andrew/dj3 uwsgi --ini uwsgi.ini
```

https://docs.docker.com/engine/reference/builder/#understand-how-cmd-and-entrypoint-interact

https://github.com/django/djangoproject.com/blob/master/docker-entrypoint.sh


