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

Cоздать и активировать виртуальное окружение:

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
