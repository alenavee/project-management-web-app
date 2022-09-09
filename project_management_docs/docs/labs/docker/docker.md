# Docker + Docker compose

## Database

`settings.py`

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'project_management_db',
        'USER': 'postgres',
        'PASSWORD': '12345pass',
        'HOST': 'db',
        'PORT': '5432',
    }
}
```

## Backend
`Dockerfile`

```
FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code/project_management_django
COPY . /code/

RUN pip install -r requirements.txt
```

`requirements.txt`
```
Django==4.0.4
djangorestframework==3.13.1
psycopg2==2.9.3
djoser==2.1.0
pandas==1.4.0
drf_yasg==1.20.0
django-cors-headers==3.11.0
```

## Frontend
`Dockerfile`

```
FROM node:lts-alpine

WORKDIR /code/project_management_vue
COPY package*.json ./
COPY . /code

EXPOSE 8080

RUN npm install -g npm
RUN npm install -g @vue/cli

RUN npm install
```

## Docker-compose
`docker-compose.yml`

```
version: '3'

services:
  db:
    image: postgres:13.0-alpine
    volumes:
      - ./data/db:/var/lib/postgresql/data/
    environment:
      - POSTGRES_DB=project_management_db
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
    ports:
      - "5432:5432"

  pgadmin:
    container_name: pgadmin4_container
    image: dpage/pgadmin4
    environment:
      PGADMIN_DEFAULT_EMAIL: admin@admin.com
      PGADMIN_DEFAULT_PASSWORD: root
    ports:
      - "5050:80"
    depends_on:
      - db


  django_rest_framework:
    build:
      context: .
      dockerfile: project_management_django/Dockerfile
    container_name: pm-backend
    command: bash -c 'sleep 10 && python manage.py runserver 0.0.0.0:8000'
    volumes:
      - .:/code
    ports:
      - "8000:8000"
    depends_on:
      - db
    links:
      - db:db

  vue:
    build:
      context: .
      dockerfile: project_management_vue/Dockerfile
    container_name: pm-frontend
    command: npm run serve
    volumes:
      - .:/code
    ports:
      - "8080:8080"
    depends_on:
      - django_rest_framework
```

## Commands
1. `docker-compose build`
2. `docker-compose up`

![Screenshot](img/docker.PNG "Screenshot")

3. `docker exec -it 5c7c2f268db1 bash`
4. `python manage.py migrate` - перенос таблиц в контейнер `postgres`

![Screenshot](img/docker2-initialmigrate.PNG "Screenshot")

# Миграции внутри контейнера

## Внесение изменений в модель
Изменена база данных: в модели `Project` значения поля `status` с `Completed` на `Finished`

## Выполнение миграций в контейнере
1. `docker exec -it 5c7c2f268db1 bash`
4. `python manage.py makemigrations`
5. `python manage.py migrate`
   
![Screenshot](img/docker3-changes.PNG "Screenshot")



# Создание пользователя postgres

![Screenshot](img/docker-pgadmin.PNG "Screenshot")


![Screenshot](img/db_new_user.PNG "Screenshot")