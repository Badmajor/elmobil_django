# Generated by Django 3.2.20 on 2023-10-09 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_car_year_until'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charging',
            name='charge_power',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Мощность зарядки'),
        ),
    ]
