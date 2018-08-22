FROM python:3.6.5-slim
MAINTAINER James Runswick <jrunswick@gmail.com>

RUN echo 'deb http://apt.postgresql.org/pub/repos/apt/ stretch-pgdg main' >> /etc/apt/sources.list.d/pgdg.list
RUN apt-get update &&\
 apt-get install -qq -y --fix-missing --no-install-recommends --allow-unauthenticated\
 build-essential\
 libpq-dev\
 postgresql-client-10

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
