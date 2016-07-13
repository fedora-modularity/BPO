FROM fedora:24
MAINTAINER Adam Samalik <asamalik@redhat.com>
ENV LANG=en_US.utf8

RUN dnf install -y python3-flask python3-redis

ADD . /code
WORKDIR /code
CMD python3 app.py
