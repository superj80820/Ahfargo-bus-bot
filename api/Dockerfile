FROM python:3.6.9

RUN pip install \
        pipenv \
        django==2.1

WORKDIR app

ADD Pipfile /app
ADD Pipfile.lock /app

RUN pipenv install