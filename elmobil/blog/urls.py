from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<slug:post_slug>', views.post_detail, name='post'),
    path('category/<slug:category_slug>/',
         views.category_posts,
         name='category_posts')

]
