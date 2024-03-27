import base64

from django.core.files.base import ContentFile
from rest_framework import serializers

from catalog.models import (AccelerationTo,
                            ArchitectureBattery, Battery, BatteryType,
                            Car, CarBody,
                            Charging, Cathode,
                            Drive, DimensionsWeight,
                            ImageCar,
                            Manufacturer, Miscellaneous,
                            NominalVoltage,
                            PackConfiguration, RangeEstimation,
                            Performance,
                            Platform,
                            PortCharge, PortLocation,
                            Segment, TypeElectric)


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
        return super().to_internal_value(data)


class ImagePackSerializer(serializers.ModelSerializer):
    image = Base64ImageField()

    class Meta:
        fields = '__all__'
        model = ImageCar


class AccelerationToSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = AccelerationTo


class DriveSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Drive


class PerformanceSerializer(serializers.ModelSerializer):
    acceleration_to_100 = AccelerationToSerializer()
    drive = DriveSerializer()

    class Meta:
        fields = '__all__'
        model = Performance


class PortChargeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = PortCharge


class PortLocationChargeSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = PortLocation


class TypeElectricSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = TypeElectric


class ChargingSerializer(serializers.ModelSerializer):
    type_port = PortChargeSerializer()
    port_location = PortLocationChargeSerializer(many=True)
    type_electric = TypeElectricSerializer()

    class Meta:
        fields = '__all__'
        model = Charging


class BatteryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = BatteryType


class ArchitectureBatterySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ArchitectureBattery


class CathodeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Cathode


class PackConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = PackConfiguration


class NominalVoltageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = NominalVoltage


class BatterySerializer(serializers.ModelSerializer):
    battery_type = BatteryTypeSerializer()
    architecture = ArchitectureBatterySerializer()
    cathode = CathodeSerializer()
    pack_configuration = PackConfigurationSerializer()
    nominal_voltage = NominalVoltageSerializer()

    class Meta:
        fields = '__all__'
        model = Battery


class RangeEstimationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = RangeEstimation


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Manufacturer


class DimensionsWeightSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = DimensionsWeight


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Platform


class CarBodySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = CarBody


class SegmentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Segment


class MiscellaneousSerializer(serializers.ModelSerializer):
    platform = PlatformSerializer()
    car_body = CarBodySerializer()
    segment = SegmentSerializer()

    class Meta:
        fields = '__all__'
        model = Miscellaneous


class CarShortSerializer(serializers.ModelSerializer):
    manufacturer = ManufacturerSerializer()
    images = ImagePackSerializer(many=True)

    class Meta:
        fields = ('id', 'title', 'manufacturer', 'images')
        model = Car


class CarSerializer(serializers.ModelSerializer):
    manufacturer = ManufacturerSerializer()
    battery = BatterySerializer()
    performance = PerformanceSerializer()
    charging = ChargingSerializer()
    charging_fast = ChargingSerializer()
    real_range_estimation = RangeEstimationSerializer()
    dimensions_weight = DimensionsWeightSerializer()
    miscellaneous = MiscellaneousSerializer()
    preceding_car = CarShortSerializer()
    next_car = CarShortSerializer()
    images = ImagePackSerializer(many=True)

    class Meta:
        exclude = ('article', )
        model = Car
