from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CarViewSet, ManufacturerViewSet

app_name = 'v1'

router = DefaultRouter()
router.register('cars', CarViewSet, basename='cars')
router.register('manufacturers', ManufacturerViewSet, basename='manufacturers')

urlpatterns = [
    path('', include(router.urls)),
]