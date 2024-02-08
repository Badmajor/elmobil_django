from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path('about/', views.about, name='about'),
    path(
        'top-100-elektromobilej-po-zapasu-hoda',
        views.TopRangeListView.as_view(),
        name='top_range_100'
    )

]

