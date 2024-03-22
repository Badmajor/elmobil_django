from rest_framework import serializers

from catalog.models import Car, Manufacturer


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Car


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Manufacturer
