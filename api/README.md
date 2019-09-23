# api

## Requirement

* Python == 3.6.9
* Django == 2.1: 為了讓Docker裡面可以使用全域的django指令 在全域與私有域pipenv裡面都安裝了django2.1 如果要修改版本請記得修改全域與私有域
* Pipenv
* Docker

## Project setup

```
docker-compose build
```

### Compiles and hot-reloads for development

```
docker-compose up
```

### Install module

```
docker-compose run app pipenv install <module>
```

## Run django command

```
docker-compose run app django-admin <command>
```

## Run django manage command

```
docker-compose run app pipenv run python manage.py <command>
```

## Run django testing

```
docker-compose run app pipenv run python manage.py test 
```