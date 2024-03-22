from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CarViewSet

router = DefaultRouter()
router.register('cars', CarViewSet, basename='cars')

urlpatterns = [
    path('v1/', include(router.urls)),
]