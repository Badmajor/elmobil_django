from rest_framework import mixins, viewsets

from catalog.models import Car, Manufacturer

from .serializers import CarSerializer, ManufacturerSerializer


class CarViewSet(mixins.RetrieveModelMixin,
                 mixins.ListModelMixin,
                 viewsets.GenericViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get_queryset(self):
        return Car.objects.select_related(
            'manufacturer',
            'real_range_estimation',
            'performance__acceleration_to_100',
            'performance__drive',
            'battery__battery_type',
            'battery__architecture',
            'battery__cathode',
            'battery__pack_configuration',
            'battery__nominal_voltage',
            'charging__type_port',
            'charging__type_electric',
            'charging_fast__type_port',
            'charging_fast__type_electric',
            'miscellaneous__platform',
            'miscellaneous__car_body',
            'miscellaneous__segment',
            'dimensions_weight',
        ).prefetch_related(
            'charging__port_location',
            'charging_fast__port_location',
            'images',
            'video_youtube'
        ).order_by('title')


class ManufacturerViewSet(mixins.RetrieveModelMixin,
                          mixins.ListModelMixin,
                          viewsets.GenericViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
