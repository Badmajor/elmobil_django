from rest_framework import serializers

from catalog.models import (AccelerationTo,
                            ArchitectureBattery, Battery, BatteryType,
                            Car, CarBody,
                            Charging, Cathode,
                            Drive, DimensionsWeight,
                            Manufacturer, Miscellaneous,
                            PackConfiguration, RangeEstimation,
                            Performance,
                            Platform,
                            PortCharge, PortLocation,
                            Segment, Side, TypeElectric)


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
    acceleration_to_200 = AccelerationToSerializer()
    drive = DriveSerializer()

    class Meta:
        fields = '__all__'
        model = Performance


class PortChargeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = PortCharge


class SideSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Side


class PortLocationChargeSerializer(serializers.ModelSerializer):
    side = SideSerializer()
    location = SideSerializer()

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


class BatterySerializer(serializers.ModelSerializer):
    battery_type = BatteryTypeSerializer()
    architecture = ArchitectureBatterySerializer()
    cathode = CathodeSerializer()
    pack_configuration = PackConfigurationSerializer()

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

    class Meta:
        fields = ('id', 'title', 'manufacturer', 'image')
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

    class Meta:
        fields = '__all__'
        model = Car
