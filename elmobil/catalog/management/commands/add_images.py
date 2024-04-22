import os
import sqlite3

from bs4 import BeautifulSoup
from django.core.files import File
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.management import BaseCommand

from catalog.models import Car, ImageCar


def _get_html_code(path_db):
    query = """
    SELECT id_car, code_page
    FROM pages_code
    WHERE img_add = 0
    LIMIT 1
    """
    with sqlite3.connect(path_db) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchone()
    return data


def _get_name_car(html_page):
    soup = BeautifulSoup(html_page, 'html.parser')
    img_main_fotorama = soup.find('div', class_='img-main fotorama')
    img_list = img_main_fotorama.find_all('a', )
    name = img_list[0].get('data-full').split('/')[-2]
    return name


def _get_images(name, path_to_images):
    images = []
    path_to_dir = os.path.join(path_to_images, name)
    for img in os.listdir(path_to_dir):
        if img.endswith('.jpg'):
            path = os.path.join(path_to_dir, img)
            images.append(path)
    return images


def update_html_code(path_db, id_car):
    query = """
    UPDATE pages_code
    SET img_add = 1
    WHERE id_car = ?
    """
    with sqlite3.connect(path_db) as conn:
        cursor = conn.cursor()
        cursor.execute(query, (id_car,))
        conn.commit()


def normalize_name(path):
    file_name = path.split('/')[-1]
    return file_name.replace('.jpg', '')


class Command(BaseCommand):
    help = 'add images'

    def handle(self, *args, **options):
        path_db = os.path.normpath(options['db_path'])
        path_to_images = options['path_to_images']
        count = 0
        while data_db := _get_html_code(path_db):
            count += 1
            self.stdout.write(f'{data_db["id_car"]}/{count}')
            car_name = _get_name_car(data_db["code_page"])
            article = data_db['id_car']
            car_obj = Car.objects.get(article=article)
            images = _get_images(car_name, path_to_images)
            for path in images:
                with open(path, 'rb') as f:
                    file = File(f)
                    obj, created = ImageCar.objects.get_or_create(name=normalize_name(file.name))
                    if created:
                        try:
                            obj.image = file
                            obj.save()
                        except Exception as ex:
                            print(ex)
                            print(type(file), obj)
                            raise ex
                car_obj.images.add(obj)
            else:
                update_html_code(path_db, article)
            car_obj.save()
            self.stdout.write(f'{data_db["id_car"]} is added images')

    def add_arguments(self, parser):
        parser.add_argument(
            'db_path',
            type=str,
            help='Path to the DB with table pages_code(SQLite)'
        )
        parser.add_argument(
            'path_to_images',
            type=str,
            help='Path to folder with img'
        )
