from django.db import models


class RangeEstimation(models.Model):
    city_cold = models.IntegerField(
        verbose_name='Город в холодную погоду'
    )
    highway_cold = models.IntegerField(
        verbose_name='Трасса в холодную погоду'
    )
    combined_cold = models.IntegerField(
        verbose_name='Смешанный в холодную погоду'
    )
    city_mild = models.IntegerField(
        verbose_name='Город в теплую погоду'
    )
    highway_mild = models.IntegerField(
        verbose_name='Трасса в теплую погоду'
    )
    combined_mild = models.IntegerField(
        verbose_name='Смешанный в теплую погоду'
    )

    class Meta:
        verbose_name = 'реальный диапазон'
        verbose_name_plural = 'Реальный диапазон'


class Manufacturer(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name='Название'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'производитель'
        verbose_name_plural = 'Производители'


class BatteryType(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name='Название'
    )

    class Meta:
        verbose_name = 'Тип батареи'
        verbose_name_plural = 'Типы батарей'


class ArchitectureBattery(models.Model):
    title = models.IntegerField(
        verbose_name='Напряжение'
    )

    class Meta:
        verbose_name = 'Архитектура батареи'
        verbose_name_plural = 'Архитектуры Батарей'


class Cathode(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name='Название'
    )

    class Meta:
        verbose_name = 'материал катода'
        verbose_name_plural = 'Материалы катода'


class PackConfiguration(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name='Название'
    )

    class Meta:
        verbose_name = 'конфигурация батареи'
        verbose_name_plural = 'Конфигурации батарей'


class NominalVoltage(models.Model):
    value_voltage = models.IntegerField(
        verbose_name='Значение'
    )

    class Meta:
        verbose_name = 'номинальный вольтаж'
        verbose_name_plural = 'Номинальный вольтаж'


class Battery(models.Model):
    nominal_capacity = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Номинальная мощность'
    )
    useable_capacity = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Полезная мощность'
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
    )
    architecture = models.ForeignKey(
        ArchitectureBattery,
        verbose_name='Напряжение',
        on_delete=models.SET_NULL,
        blank=True, null=True,
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
    )

    class Meta:
        default_related_name = 'battery'
        verbose_name = 'батарея'
        verbose_name_plural = 'Батареи'


class AccelerationTo(models.Model):
    time = models.DecimalField(
        max_digits=3,
        decimal_places=1
    )

    class Meta:
        verbose_name = 'время разгона'
        verbose_name_plural = 'Время разгона'


class Drive(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name='Название'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'привод'
        verbose_name_plural = 'Приводы'


class Performance(models.Model):
    acceleration_to_100 = models.ForeignKey(
        AccelerationTo,
        verbose_name='Разгон до 100км/ч',
        on_delete=models.SET_NULL,
        blank=True, null=True,
    )
    acceleration_to_200 = models.ForeignKey(
        AccelerationTo,
        blank=True, null=True,
        verbose_name='Разгон до 200км/ч',
        on_delete=models.SET_NULL,
        related_name='performance_to_200'
    )
    top_speed = models.IntegerField(
        verbose_name='Максимальная скорость'
    )
    electric_range = models.IntegerField(
        verbose_name='Запас хода'
    )
    total_power = models.IntegerField(
        verbose_name='Мощность'
    )
    total_torque = models.IntegerField(
        verbose_name='Крутящий момент'
    )
    drive = models.ForeignKey(
        Drive,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        verbose_name='Привод'
    )

    class Meta:
        default_related_name = 'performance'
        verbose_name = 'производительность'
        verbose_name_plural = 'Производительность'


class PortCharge(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name='Название'
    )

    class Meta:
        verbose_name = 'тип порта зарядки'
        verbose_name_plural = 'Типы портов зарядки'


class Side(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name='Название'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'сторона'
        verbose_name_plural = 'Стороны'


class PortLocation(models.Model):
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


class TypeElectric(models.Model):
    title = models.CharField(
        max_length=6,
        verbose_name='Название'
    )

    class Meta:
        verbose_name = 'тип электричества'
        verbose_name_plural = 'Типы электричества'


class Charging(models.Model):
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
        verbose_name='Мощность зарядки'
    )
    type_electric = models.ForeignKey(
        TypeElectric,
        verbose_name='Тип электричества',
        on_delete=models.SET_NULL,
        blank=True, null=True,
    )
    charge_time = models.TimeField(
        blank=True, null=True,
    )
    charge_speed = models.IntegerField(
        blank=True
    )

    class Meta:
        default_related_name = 'charging'
        verbose_name = 'зарядка'
        verbose_name_plural = 'Зарядка'


class DimensionsWeight(models.Model):
    length = models.IntegerField(
        verbose_name='Длина',
        null=True,
    )
    width = models.IntegerField(
        verbose_name='Ширина',
        null=True,
    )
    width_with_mirrors = models.IntegerField(
        verbose_name='Ширина с зеркалами',
        null=True,
    )
    height = models.IntegerField(
        verbose_name='Высота',
        null=True,
    )
    wheelbase = models.IntegerField(
        verbose_name='Колесная база',
        null=True,
    )
    weight_unladen = models.IntegerField(
        verbose_name='Вес без нагрузки',
        null=True,
    )
    gross_weight = models.IntegerField(
        verbose_name='Полная масса',
        null=True,
    )
    payload = models.IntegerField(
        verbose_name='Грузоподъемность',
        null=True,
    )
    cargo_volume = models.IntegerField(
        verbose_name='Объем багажника',
        null=True,
    )
    cargo_volume_frunk = models.IntegerField(
        verbose_name='Объем переднего багажника',
        null=True,
    )
    tow_hitch = models.BooleanField(
        null=True,
        blank=True,
        verbose_name='Возможность установить фаркоп'
    )

    class Meta:
        verbose_name = 'размер и вес'
        verbose_name_plural = 'Размеры и вес'


class Platform(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name='Название'
    )

    class Meta:
        verbose_name = 'тип электричества'
        verbose_name_plural = 'Типы электричества'


class CarBody(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name='Название'
    )

    class Meta:
        verbose_name = 'тип электричества'
        verbose_name_plural = 'Типы электричества'


class Segment(models.Model):
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


class Miscellaneous(models.Model):
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
        verbose_name_plural = 'Дополнительно'


class Car(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name='Название'
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
        verbose_name='Безопасность',
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

    def increase_view_count(self):
        self.view_count += 1
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        default_related_name = 'cars'
        verbose_name = 'электромобиль'
        verbose_name_plural = 'Электромобили'
