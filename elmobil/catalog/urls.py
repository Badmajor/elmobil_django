from django.urls import path

from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.CarsListView.as_view(), name='car_list'),
    path('catalog/<int:pk>/<slug:slug>/', views.CarDetailView.as_view(), name='car_detail'),
    path('catalog/<int:pk>/', views.CarDetailView.as_view(), name='car_detail_pk'),
    path(
        'catalog/manufacturer/<slug:slug>/',
        views.ManufacturerDetailView.as_view(),
        name='manufacturer'
    ),
]
