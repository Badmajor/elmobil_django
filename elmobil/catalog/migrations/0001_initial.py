# Generated by Django 5.0.3 on 2024-03-25 11:39

import catalog.mixins
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccelerationTo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DecimalField(decimal_places=1, max_digits=3)),
            ],
            options={
                'verbose_name': 'время разгона',
                'verbose_name_plural': 'Время разгона',
            },
        ),
        migrations.CreateModel(
            name='ArchitectureBattery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.IntegerField(verbose_name='Напряжение')),
            ],
            options={
                'verbose_name': 'Архитектура батареи',
                'verbose_name_plural': 'Архитектуры Батарей',
            },
            bases=(catalog.mixins.StrTitleMixin, models.Model),
        ),
        migrations.CreateModel(
            name='BatteryType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тип батареи',
                'verbose_name_plural': 'Типы батарей',
            },
            bases=(catalog.mixins.StrTitleMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CarBody',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'тип электричества',
                'verbose_name_plural': 'Типы электричества',
            },
            bases=(catalog.mixins.StrTitleMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Cathode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'материал катода',
                'verbose_name_plural': 'Материалы катода',
            },
            bases=(catalog.mixins.StrTitleMixin, models.Model),
        ),
        migrations.CreateModel(
            name='DimensionsWeight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', models.IntegerField(help_text='мм', null=True, verbose_name='Длина')),
                ('width', models.IntegerField(help_text='мм', null=True, verbose_name='Ширина')),
                ('width_with_mirrors', models.IntegerField(help_text='мм', null=True, verbose_name='Ширина с зеркалами')),
                ('height', models.IntegerField(help_text='мм', null=True, verbose_name='Высота')),
                ('wheelbase', models.IntegerField(help_text='мм', null=True, verbose_name='Колесная база')),
                ('weight_unladen', models.IntegerField(help_text='кг.', null=True, verbose_name='Вес без нагрузки')),
                ('gross_weight', models.IntegerField(help_text='кг.', null=True, verbose_name='Полная масса')),
                ('payload', models.IntegerField(help_text='кг.', null=True, verbose_name='Грузоподъемность')),
                ('cargo_volume', models.IntegerField(help_text='л.', null=True, verbose_name='Объем багажника')),
                ('cargo_volume_frunk', models.IntegerField(help_text='л.', null=True, verbose_name='Объем переднего багажника')),
                ('tow_hitch', models.BooleanField(blank=True, null=True, verbose_name='Возможность установить фаркоп')),
            ],
            options={
                'verbose_name': 'размер и вес',
                'verbose_name_plural': 'Габариты и Вес',
            },
            bases=(models.Model, catalog.mixins.VerboseNamePluralMixin, catalog.mixins.IterMixin),
        ),
        migrations.CreateModel(
            name='Drive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'привод',
                'verbose_name_plural': 'Приводы',
            },
            bases=(catalog.mixins.StrTitleMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ImageCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='car_images', verbose_name='Фото')),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Название')),
                ('description', models.TextField(blank=True, default=None, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'производитель',
                'verbose_name_plural': 'Производители',
            },
            bases=(catalog.mixins.StrTitleMixin, models.Model),
        ),
        migrations.CreateModel(
            name='NominalVoltage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.IntegerField(verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'номинальный вольтаж',
                'verbose_name_plural': 'Номинальный вольтаж',
            },
            bases=(catalog.mixins.StrTitleMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PackConfiguration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'конфигурация батареи',
                'verbose_name_plural': 'Конфигурации батарей',
            },
            bases=(catalog.mixins.StrTitleMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'тип электричества',
                'verbose_name_plural': 'Типы электричества',
            },
            bases=(catalog.mixins.StrTitleMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PortCharge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'тип порта зарядки',
                'verbose_name_plural': 'Типы портов зарядки',
            },
            bases=(catalog.mixins.StrTitleMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PortLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'расположение порта',
                'verbose_name_plural': 'Расположение порта',
            },
            bases=(catalog.mixins.StrTitleMixin, models.Model),
        ),
        migrations.CreateModel(
            name='RangeEstimation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_cold', models.IntegerField(help_text='км.', verbose_name='Город в холодную погоду')),
                ('highway_cold', models.IntegerField(help_text='км.', verbose_name='Трасса в холодную погоду')),
                ('combined_cold', models.IntegerField(help_text='км.', verbose_name='Смешанный в холодную погоду')),
                ('city_mild', models.IntegerField(help_text='км.', verbose_name='Город в теплую погоду')),
                ('highway_mild', models.IntegerField(help_text='км.', verbose_name='Трасса в теплую погоду')),
                ('combined_mild', models.IntegerField(help_text='км.', verbose_name='Смешанный в теплую погоду')),
            ],
            options={
                'verbose_name': 'реальный диапазон',
                'verbose_name_plural': 'Реальный диапазон',
            },
            bases=(models.Model, catalog.mixins.VerboseNamePluralMixin, catalog.mixins.IterMixin),
        ),
        migrations.CreateModel(
            name='Segment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Название')),
                ('char_class', models.CharField(max_length=10, verbose_name='Класс')),
            ],
            options={
                'verbose_name': 'тип электричества',
                'verbose_name_plural': 'Типы электричества',
            },
            bases=(catalog.mixins.StrTitleMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Side',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'сторона',
                'verbose_name_plural': 'Стороны',
            },
            bases=(catalog.mixins.StrTitleMixin, models.Model),
        ),
        migrations.CreateModel(
            name='TypeElectric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=6, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'тип электричества',
                'verbose_name_plural': 'Типы электричества',
            },
            bases=(catalog.mixins.StrTitleMixin, models.Model),
        ),
        migrations.CreateModel(
            name='VideoUrlYouTube',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(verbose_name='Ссылка на видео YouTube')),
            ],
        ),
        migrations.CreateModel(
            name='Battery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nominal_capacity', models.DecimalField(decimal_places=2, help_text='кВт⋅ч', max_digits=10, verbose_name='Номинальная мощность')),
                ('usable_capacity', models.DecimalField(decimal_places=2, help_text='кВт⋅ч', max_digits=10, verbose_name='Полезная мощность')),
                ('number_of_cells', models.IntegerField(blank=True, help_text='шт.', verbose_name='Количество ячеек')),
                ('architecture', models.ForeignKey(blank=True, help_text='V', null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.architecturebattery', verbose_name='Напряжение')),
                ('battery_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.batterytype', verbose_name='Тип батареи')),
                ('cathode', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.cathode', verbose_name='Катод')),
                ('nominal_voltage', models.ForeignKey(blank=True, help_text='В', null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.nominalvoltage', verbose_name='Вольтаж')),
                ('pack_configuration', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.packconfiguration', verbose_name='Конфигурация')),
            ],
            options={
                'verbose_name': 'батарея',
                'verbose_name_plural': 'Батарея',
                'default_related_name': 'battery',
            },
            bases=(models.Model, catalog.mixins.VerboseNamePluralMixin, catalog.mixins.IterMixin),
        ),
        migrations.CreateModel(
            name='Miscellaneous',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seats', models.IntegerField(verbose_name='Количество мест')),
                ('isofix', models.BooleanField(blank=True, null=True, verbose_name='Крепление для детского кресла')),
                ('isofix_count', models.IntegerField(blank=True, null=True, verbose_name='Количество детских кресел')),
                ('turning_circle', models.DecimalField(decimal_places=1, max_digits=3, null=True, verbose_name='Радиус поворота')),
                ('roof_rails', models.BooleanField(blank=True, null=True, verbose_name='Рейлинги')),
                ('special_ev_platform', models.BooleanField(blank=True, null=True, verbose_name='Платформа для электромобилей?')),
                ('car_body', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.carbody', verbose_name='Тип кузова')),
                ('platform', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.platform', verbose_name='Платформа')),
                ('segment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.segment', verbose_name='Сегмент')),
            ],
            options={
                'verbose_name': 'дополнительно',
                'verbose_name_plural': 'Разное',
                'default_related_name': 'miscellaneous',
            },
            bases=(models.Model, catalog.mixins.VerboseNamePluralMixin, catalog.mixins.IterMixin),
        ),
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top_speed', models.IntegerField(help_text='Км/ч', verbose_name='Максимальная скорость')),
                ('electric_range', models.IntegerField(help_text='Км', verbose_name='Запас хода')),
                ('total_power', models.IntegerField(help_text='кВт', verbose_name='Мощность')),
                ('total_torque', models.IntegerField(help_text='Нм', verbose_name='Крутящий момент')),
                ('acceleration_to_100', models.ForeignKey(blank=True, help_text='с.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.accelerationto', verbose_name='Разгон до 100км/ч')),
                ('acceleration_to_200', models.ForeignKey(blank=True, help_text='с.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='performance_to_200', to='catalog.accelerationto', verbose_name='Разгон до 200км/ч')),
                ('drive', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.drive', verbose_name='Привод')),
            ],
            options={
                'verbose_name': 'производительность',
                'verbose_name_plural': 'Производительность',
                'default_related_name': 'performance',
            },
            bases=(models.Model, catalog.mixins.VerboseNamePluralMixin, catalog.mixins.IterMixin),
        ),
        migrations.CreateModel(
            name='Charging',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charge_power', models.DecimalField(decimal_places=2, help_text='кВт⋅ч', max_digits=10, verbose_name='Мощность зарядки')),
                ('charge_time', models.TimeField(blank=True, help_text='ч:м:с', null=True, verbose_name='Время зарядки (до 80%)')),
                ('charge_speed', models.IntegerField(blank=True, help_text='км/ч', verbose_name='Скорость зарядки')),
                ('type_port', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.portcharge', verbose_name='Тип порта')),
                ('port_location', models.ManyToManyField(blank=True, to='catalog.portlocation', verbose_name='Расположение порта')),
                ('type_electric', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.typeelectric', verbose_name='Тип электричества')),
            ],
            options={
                'verbose_name': 'зарядка',
                'verbose_name_plural': 'Зарядка',
                'default_related_name': 'charging',
            },
            bases=(models.Model, catalog.mixins.VerboseNamePluralMixin, catalog.mixins.IterMixin),
        ),
        migrations.AddField(
            model_name='portlocation',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='port_location_location', to='catalog.side', verbose_name='Расположение'),
        ),
        migrations.AddField(
            model_name='portlocation',
            name='side',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='port_location_side', to='catalog.side', verbose_name='Сторона'),
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Название')),
                ('slug', models.CharField(max_length=256, verbose_name='Slug')),
                ('description', models.TextField(blank=True, default=None, null=True, verbose_name='Описание')),
                ('view_count', models.IntegerField(default=0, verbose_name='Просмотры')),
                ('year_release', models.IntegerField(null=True, verbose_name='Год начала выпуска')),
                ('year_until', models.IntegerField(default=None, null=True, verbose_name='Выпускался до')),
                ('battery', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.battery', verbose_name='Батарея')),
                ('next_car', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next_model', to='catalog.car', verbose_name='Предыдущая модель')),
                ('preceding_car', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='preceding_model', to='catalog.car', verbose_name='Предыдущая модель')),
                ('charging', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.charging', verbose_name='Зарядка')),
                ('charging_fast', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cars_fast_charge', to='catalog.charging', verbose_name='Быстрая зарядка')),
                ('dimensions_weight', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.dimensionsweight', verbose_name='Габариты и вес')),
                ('images', models.ManyToManyField(to='catalog.imagecar')),
                ('manufacturer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.manufacturer', verbose_name='Производитель')),
                ('miscellaneous', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.miscellaneous', verbose_name='Дополнительно')),
                ('performance', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.performance', verbose_name='Производительность')),
                ('real_range_estimation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.rangeestimation', verbose_name='Оценка реального диапазона')),
                ('video_youtube', models.ManyToManyField(to='catalog.videourlyoutube')),
            ],
            options={
                'verbose_name': 'электромобиль',
                'verbose_name_plural': 'Электромобили',
                'default_related_name': 'cars',
            },
            bases=(catalog.mixins.StrTitleMixin, models.Model),
        ),
    ]
