FROM python:3.6

WORKDIR /app

ADD $PWD/api/Pipfile /app/
ADD $PWD/api/Pipfile.lock /app/

RUN pip install -U \
    pipenv
RUN pipenv install