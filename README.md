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
sudo docker compose exec backend python manage.py migrate
```

```bash
python3 -m venv env
source env/bin/activate
```
Установить зависимости из файла requirements.txt:
```bash
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

создать файл .env  со следующим содержание:
```bash
SECRET_KEY_DJANGO='django-secret'
DEBUG=False
ALLOWED_HOSTS=127.0.0.1
STATIC_ROOT='<путь до каталога где планируете размещать статику>'
```

Выполнить миграции:
```bash
python3 manage.py migrate
```
Запустить проект:
```bash
python3 manage.py runserver
```

# В процессе:

## Написать API для перехода на SPA

## Увеличение базы электромобилей до 700 шт.

## Разработать и внедрить автогенерацию описания электромобилей

## Реализовать CI/CD
