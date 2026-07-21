from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path('about/', views.about, name='about'),
    path(
        'top-100-elektromobilej-po-zapasu-hoda',
        views.TopRangeListView.as_view(),
        name='top_range_100'
    ),
    path(
        'top-100-elektromobilej-po-skorosti-zaryadki',
        views.TopChargeTimeListView.as_view(),
        name='top_time_charge_100'
    ),
    path('charge_cost/', views.charge_cost, name='charge_cost'),
    path(
        "сколько-стоит-зарядить-электромобил/", views.charge_cost, name="charge_cost_redirect"
    ),
]
