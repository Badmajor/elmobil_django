# Generated by Django 3.2.20 on 2023-09-13 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20230913_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_slug',
            field=models.CharField(default=models.CharField(max_length=75), max_length=75),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=75),
        ),
    ]
