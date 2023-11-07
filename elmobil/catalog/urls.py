from django.urls import path

from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.CarsListView.as_view(), name='car_list'),
    path('<int:pk>/<slug:slug>/', views.CarDetailView.as_view(), name='car_detail'),
    path('<int:pk>/', views.CarDetailView.as_view(), name='car_detail_pk'),
    path(
        'manufacturer/<slug:slug>/',
        views.ManufacturerDetailView.as_view(),
        name='manufacturer'
    ),
]
