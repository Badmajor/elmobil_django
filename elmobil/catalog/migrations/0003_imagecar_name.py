# Generated by Django 5.0.3 on 2024-04-22 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_imagecar_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagecar',
            name='name',
            field=models.CharField(default=1, max_length=256, verbose_name='Название'),
            preserve_default=False,
        ),
    ]
