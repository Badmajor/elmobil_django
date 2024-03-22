from rest_framework import viewsets

from catalog.models import Car


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()