# Generated by Django 3.2.20 on 2023-09-15 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20230913_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_of_change',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_of_create',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
