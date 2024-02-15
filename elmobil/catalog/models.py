import os

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from .mixins import VerboseNamePluralMixin, StrTitleMixin, IterMixin


class RangeEstimation(models.Model, VerboseNamePluralMixin, IterMixin):
    city_cold = models.IntegerField(
        verbose_name='Город в холодную погоду',
        help_text='км.'
    )
    highway_cold = models.IntegerField(
        verbose_name='Трасса в холодную погоду',
        help_text='км.'
    )
    combined_cold = models.IntegerField(
        verbose_name='Смешанный в холодную погоду',
        help_text='км.'
    )
    city_mild = models.IntegerField(
        verbose_name='Город в теплую погоду',
        help_text='км.'
    )
    highway_mild = models.IntegerField(
        verbose_name='Трасса в теплую погоду',
        help_text='км.'
    )
    combined_mild = models.IntegerField(
        verbose_name='Смешанный в теплую погоду',
        help_text='км.'
    )

    class Meta:
        verbose_name = 'реальный диапазон'
        verbose_name_plural = 'Реальный диапазон'


class Manufacturer(StrTitleMixin, models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name='Название'
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True, null=True,
        default=None,
    )

    class Meta:
        verbose_name = 'производитель'
        verbose_name_plural = 'Производители'

    def get_absolute_url(self):
        slug = slugify(self.title)
        return reverse('catalog:manufacturer', args=[slug])


class BatteryType(StrTitleMixin, models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name='Название'
    )

    class Meta:
        verbose_name = 'Тип батареи'
        verbose_name_plural = 'Типы батарей'


class ArchitectureBattery(StrTitleMixin, models.Model):
    title = models.IntegerField(
        verbose_name='Напряжение'
    )

    class Meta:
        verbose_name = 'Архитектура батареи'
        verbose_name_plural = 'Архитектуры Батарей'


class Cathode(StrTitleMixin, models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name='Название'
    )

    class Meta:
        verbose_name = 'материал катода'
        verbose_name_plural = 'Материалы катода'


class PackConfiguration(StrTitleMixin, models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name='Значение'
    )

    class Meta:
        verbose_name = 'конфигурация батареи'
        verbose_name_plural = 'Конфигурации батарей'


class NominalVoltage(StrTitleMixin, models.Model):
    title = models.IntegerField(
        verbose_name='Значение'
    )

    class Meta:
        verbose_name = 'номинальный вольтаж'
        verbose_name_plural = 'Номинальный вольтаж'


class Battery(models.Model, VerboseNamePluralMixin, IterMixin):
    nominal_capacity = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Номинальная мощность',
        help_text='кВт⋅ч',
    )
    usable_capacity = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Полезная мощность',
        help_text='кВт⋅ч',
    )
    battery_type = models.ForeignKey(
        BatteryType,
        verbose_name='Тип батареи',
        on_delete=models.SET_NULL,
        blank=True, null=True,
    )
    number_of_cells = models.IntegerField(
        verbose_name='Количество ячеек',
        blank=True,
        help_text='шт.',
    )
    architecture = models.ForeignKey(
        ArchitectureBattery,
        verbose_name='Напряжение',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text='V',
    )
    cathode = models.ForeignKey(
        Cathode,
        verbose_name='Катод',
        on_delete=models.SET_NULL,
        blank=True, null=True,
    )
    pack_configuration = models.ForeignKey(
        PackConfiguration,
        verbose_name='Конфигурация',
        on_delete=models.SET_NULL,
        blank=True, null=True,
    )
    nominal_voltage = models.ForeignKey(
        NominalVoltage,
        verbose_name='Вольтаж',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text='В',
    )

    class Meta:
        default_related_name = 'battery'
        verbose_name = 'батарея'
        verbose_name_plural = 'Батарея'


class AccelerationTo(models.Model):
    time = models.DecimalField(
        max_digits=3,
        decimal_places=1
    )

    def __str__(self):
        return str(self.time)

    class Meta:
        verbose_name = 'время разгона'
        verbose_name_plural = 'Время разгона'


class Drive(StrTitleMixin, models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name='Название'
    )

    class Meta:
        verbose_name = 'привод'
        verbose_name_plural = 'Приводы'


class Performance(models.Model, VerboseNamePluralMixin, IterMixin):

    acceleration_to_100 = models.ForeignKey(
        AccelerationTo,
        help_text='с.',
        verbose_name='Разгон до 100км/ч',
        on_delete=models.SET_NULL,
        blank=True, null=True,
    )
    acceleration_to_200 = models.ForeignKey(
        AccelerationTo,
        help_text='с.',
        blank=True, null=True,
        verbose_name='Разгон до 200км/ч',
        on_delete=models.SET_NULL,
        related_name='performance_to_200'
    )
    top_speed = models.IntegerField(
        verbose_name='Максимальная скорость',
        help_text='Км/ч',
    )
    electric_range = models.IntegerField(
        verbose_name='Запас хода',
        help_text='Км',
    )
    total_power = models.IntegerField(
        help_text='кВт',
        verbose_name='Мощность'
    )
    total_torque = models.IntegerField(
        help_text='Нм',
        verbose_name='Крутящий момент'
    )
    drive = models.ForeignKey(
        Drive,
        help_text='',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        verbose_name='Привод'
    )

    class Meta:
        default_related_name = 'performance'
        verbose_name = 'производительность'
        verbose_name_plural = 'Производительность'


class PortCharge(StrTitleMixin, models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name='Название'
    )

    class Meta:
        verbose_name = 'тип порта зарядки'
        verbose_name_plural = 'Типы портов зарядки'


class Side(StrTitleMixin, models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name='Название'
    )

    class Meta:
        verbose_name = 'сторона'
        verbose_name_plural = 'Стороны'


class PortLocation(StrTitleMixin, models.Model):
    side = models.ForeignKey(
        Side,
        verbose_name='Сторона',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name='port_location_side'
    )
    location = models.ForeignKey(
        Side,
        verbose_name='Расположение',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name='port_location_location'
    )

    def __str__(self):
        return f'{self.side} - {self.location}'

    class Meta:
        verbose_name = 'расположение порта'
        verbose_name_plural = 'Расположение порта'


class TypeElectric(StrTitleMixin, models.Model):
    title = models.CharField(
        max_length=6,
        verbose_name='Название'
    )

    class Meta:
        verbose_name = 'тип электричества'
        verbose_name_plural = 'Типы электричества'


class Charging(models.Model, VerboseNamePluralMixin, IterMixin):
    type_port = models.ForeignKey(
        PortCharge,
        verbose_name='Тип порта',
        on_delete=models.SET_NULL,
        blank=True, null=True,
    )
    port_location = models.ForeignKey(
        PortLocation,
        verbose_name='Расположение порта',
        on_delete=models.SET_NULL,
        blank=True, null=True,
    )
    port_location_2 = models.ForeignKey(
        PortLocation,
        verbose_name='Расположение порта_2',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name='charging_2'
    )
    charge_power = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Мощность зарядки',
        help_text='кВт⋅ч'

    )
    type_electric = models.ForeignKey(
        TypeElectric,
        verbose_name='Тип электричества',
        on_delete=models.SET_NULL,
        blank=True, null=True,
    )
    charge_time = models.TimeField(
        blank=True,
        null=True,
        verbose_name='Время зарядки (до 80%)',
        help_text='ч:м:с'
    )
    charge_speed = models.IntegerField(
        blank=True,
        help_text='км/ч',
        verbose_name='Скорость зарядки'
    )

    class Meta:
        default_related_name = 'charging'
        verbose_name = 'зарядка'
        verbose_name_plural = 'Зарядка'


class DimensionsWeight(models.Model, VerboseNamePluralMixin, IterMixin):
    length = models.IntegerField(
        verbose_name='Длина',
        null=True,
        help_text='мм'
    )
    width = models.IntegerField(
        verbose_name='Ширина',
        null=True,
        help_text='мм'
    )
    width_with_mirrors = models.IntegerField(
        verbose_name='Ширина с зеркалами',
        null=True,
        help_text='мм'
    )
    height = models.IntegerField(
        verbose_name='Высота',
        null=True,
        help_text='мм'
    )
    wheelbase = models.IntegerField(
        verbose_name='Колесная база',
        null=True,
        help_text='мм'
    )
    weight_unladen = models.IntegerField(
        verbose_name='Вес без нагрузки',
        null=True,
        help_text='кг.'
    )
    gross_weight = models.IntegerField(
        verbose_name='Полная масса',
        null=True,
        help_text='кг.'
    )
    payload = models.IntegerField(
        verbose_name='Грузоподъемность',
        null=True,
        help_text='кг.'
    )
    cargo_volume = models.IntegerField(
        verbose_name='Объем багажника',
        null=True,
        help_text='л.'
    )
    cargo_volume_frunk = models.IntegerField(
        verbose_name='Объем переднего багажника',
        null=True,
        help_text='л.'
    )
    tow_hitch = models.BooleanField(
        null=True,
        blank=True,
        verbose_name='Возможность установить фаркоп'
    )

    class Meta:
        verbose_name = 'размер и вес'
        verbose_name_plural = 'Габариты и Вес'


class Platform(StrTitleMixin, models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name='Название'
    )

    class Meta:
        verbose_name = 'тип электричества'
        verbose_name_plural = 'Типы электричества'


class CarBody(StrTitleMixin, models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name='Название'
    )

    class Meta:
        verbose_name = 'тип электричества'
        verbose_name_plural = 'Типы электричества'


class Segment(StrTitleMixin, models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name='Название'
    )
    char_class = models.CharField(
        max_length=10,
        verbose_name='Класс'
    )

    class Meta:
        verbose_name = 'тип электричества'
        verbose_name_plural = 'Типы электричества'


class Miscellaneous(models.Model, VerboseNamePluralMixin, IterMixin):
    seats = models.IntegerField(
        verbose_name='Количество мест',
    )
    isofix = models.BooleanField(
        verbose_name='Крепление для детского кресла',
        null=True, blank=True,
    )
    isofix_count = models.IntegerField(
        verbose_name='Количество детских кресел',
        null=True, blank=True,
    )
    turning_circle = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        verbose_name='Радиус поворота',
        null=True
    )
    platform = models.ForeignKey(
        Platform,
        verbose_name='Платформа',
        on_delete=models.SET_NULL,
        null=True, blank=True,
    )
    car_body = models.ForeignKey(
        CarBody,
        verbose_name='Тип кузова',
        on_delete=models.SET_NULL,
        null=True, blank=True,
    )
    segment = models.ForeignKey(
        Segment,
        verbose_name='Сегмент',
        on_delete=models.SET_NULL,
        null=True, blank=True,
    )
    roof_rails = models.BooleanField(
        verbose_name='Рейлинги',
        null=True, blank=True,
    )
    special_ev_platform = models.BooleanField(
        verbose_name='Платформа для электромобилей?',
        null=True, blank=True,
    )

    class Meta:
        default_related_name = 'miscellaneous'
        verbose_name = 'дополнительно'
        verbose_name_plural = 'Разное'


class Car(StrTitleMixin, models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name='Название',
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True, null=True,
        default=None,
    )
    manufacturer = models.ForeignKey(
        Manufacturer,
        verbose_name='Производитель',
        on_delete=models.SET_NULL,
        blank=True, null=True,
    )
    performance = models.ForeignKey(
        Performance,
        verbose_name='Производительность',
        on_delete=models.SET_NULL,
        blank=True, null=True,
    )
    battery = models.ForeignKey(
        Battery,
        verbose_name='Батарея',
        on_delete=models.SET_NULL,
        blank=True, null=True,
    )
    charging = models.ForeignKey(
        Charging,
        verbose_name='Зарядка',
        on_delete=models.SET_NULL,
        blank=True, null=True,
    )
    charging_fast = models.ForeignKey(
        Charging,
        verbose_name='Быстрая зарядка',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name='cars_fast_charge'
    )
    real_range_estimation = models.ForeignKey(
        RangeEstimation,
        verbose_name='Оценка реального диапазона',
        blank=True, null=True,
        on_delete=models.SET_NULL,
    )
    dimensions_weight = models.ForeignKey(
        DimensionsWeight,
        verbose_name='Габариты и вес',
        blank=True, null=True,
        on_delete=models.SET_NULL,
    )
    miscellaneous = models.ForeignKey(
        Miscellaneous,
        verbose_name='Дополнительно',
        on_delete=models.SET_NULL,
        blank=True, null=True,
    )
    view_count = models.IntegerField(
        default=0,
        verbose_name='Просмотры'
    )
    year_release = models.IntegerField(
        verbose_name='Год начала выпуска',
        null=True
    )
    year_until = models.IntegerField(
        verbose_name='Выпускался до',
        null=True, default=None,
    )
    image = models.ImageField(
        'Фото',
        upload_to='car_images',
        blank=True
    )

    preceding_car = models.ForeignKey(
        'self',
        verbose_name='Предыдущая модель',
        null=True,
        default=None,
        on_delete=models.SET_NULL,
        related_name='preceding_model'
    )

    next_car = models.ForeignKey(
        'self',
        verbose_name='Предыдущая модель',
        null=True,
        default=None,
        on_delete=models.SET_NULL,
        related_name='next_model'
    )

    @property
    def img_list(self):
        img_list = []
        try:
            files = os.listdir(f'{settings.BASE_DIR}/static/img/car_img/{self.pk}/')
            for file in files:
                if 'jpg' in file:
                    img_list.append(file)
            return img_list
        except FileNotFoundError:
            return None

    def increase_view_count(self):
        self.view_count += 1
        self.save()

    class Meta:
        default_related_name = 'cars'
        verbose_name = 'электромобиль'
        verbose_name_plural = 'Электромобили'

    def get_absolute_url(self):
        slug = slugify(self.title)
        return reverse('catalog:car_detail', args=[self.pk, slug])


