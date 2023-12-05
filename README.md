# Тестовое задания для Fructorum
___
**Cервис который хранит ссылки пользователей(закладки) на веб-сайты.**


## Требования

Для запуска этого проекта вам потребуется установить следующее:
- Docker: [Ссылка на установку Docker](https://docs.docker.com/get-docker/)
- Docker Compose: [Ссылка на установку Docker Compose](https://docs.docker.com/compose/install/)

## Запуск проекта

1. Склонируйте репозиторий:

```bash
https://github.com/Asada19/fructorum_test_task.git
```

2. Добавьте зависимости в .env

```bash
cp example.env .env
```
```dotenv
POSTGRES_DB='book_mark_db'
POSTGRES_USER='my_user'
POSTGRES_PASSWORD='my_password'
POSTGRES_HOST=postgres
POSTGRES_PORT=5432

SECRET_KEY='secret_key'
DEBUG=
ALLOWED_HOSTS='*'
```

3. Запустите docker-compose:

```bash
docker-compose up --build
```

---

## Enpoints:
##### bookmark
![My image](https://i.ibb.co/LS6z9Kp/2023-12-05-17-16-03.png)
##### user authentication
![My image](https://i.ibb.co/zPkgJLS/2023-12-05-17-18-52.png)
##### database diagram
![My image](https://i.ibb.co/0cqb9Zn/2023-12-05-11-12-50.png)
___
### *Stack:*
- `python: 3.8.16`
- `djangoDjango:4.2.8`
- `djangorestframework:3.14.0`


`затраченное время: 5-7 часов`
