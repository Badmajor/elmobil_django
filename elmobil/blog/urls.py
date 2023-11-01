from django.urls import path
from django.views.generic import RedirectView

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<slug:post_slug>', views.post_detail, name='post'),
    path('category/<slug:category_slug>/',
         views.category_posts,
         name='category_posts'),
    path(
        'транспортный-налог-на-электромобили/',
        RedirectView.as_view(
            url='/post/transportnyy-nalog-na-elektromobili',
            permanent=True
        ),
    ),
    path(
        'заказавшим-tesla-за-35-000-придется-проявить-те/',
        RedirectView.as_view(
            url='/post/zakazavshim-tesla-za-35-000-proyavit-te',
            permanent=True
        ),
    ),
    path(
        'jaguar-i-pace-против-tesla-model-x-кто-кого/',
        RedirectView.as_view(
            url='/post/jaguar-i-pace-protiv-tesla-model-x-kto-kogo',
            permanent=True
        ),
    ),
]
