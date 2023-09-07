from django.urls import path

from elmobil.pages import views

app_name = 'pages'

urlpatterns = [
    path('', views.index, name='index')

]

