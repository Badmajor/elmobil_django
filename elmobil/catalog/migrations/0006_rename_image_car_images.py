# Generated by Django 3.2.20 on 2024-03-22 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_rename_image_imagecar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='image',
            new_name='images',
        ),
    ]
