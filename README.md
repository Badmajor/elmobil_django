[![Elmobil.ru Workflow](https://github.com/Badmajor/elmobil_django/actions/workflows/main.yml/badge.svg)](https://github.com/Badmajor/elmobil_django/actions/workflows/main.yml)

# О проекте

elmobil.ru задумывался как блог про электромобили, 
но в итоге принял решение сделать каталог электромобилей
с подробными характеристиками. На момент создания в рунете 
аналогов не было.

## Как запустить проект:
Клонировать репозиторий и перейти в каталог:
```bash
git clone git@github.com:Badmajor/elmobil_django.git
```
Перейти в каталог с docker-compose.yml
```bash
cd elmobil_django/infra_test/
```
Подготовить файл .env
```bash
cp .env.example .env
```
Упаковать и запустить контейнеры:
```bash
sudo docker compose up --build -d
```
Выполнить миграции:
```bash
sudo docker compose exec backend python manage.py migrate
```
Собрать статику и скопировать статику:
```bash
sudo docker compose exec backend python manage.py collectstatic
sudo docker compose exec backend cp -r /elmobil/static/. /static/
```
Наполнить базу данных:
```bash
sudo docker compose exec backend python manage.py loaddata ./temp_data/example_data.json
```
Каталог будет доступен по адресу:
http://127.0.0.1:8777/

## Вход в админ зону:

- http://127.0.0.1:8777/admin/

Данные для superusera:
- email: admin@admin.ru
- pass: admin

## Документация API:

- http://127.0.0.1:8777/redoc/


## Данные тестового пользователя:

Тестовый пользователь:
- email: test@test.ru
- pass: testpassword
