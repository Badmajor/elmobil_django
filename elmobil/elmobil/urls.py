from django.conf import settings
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include

from blog.sitemap import PostSitemap, AutorSitemap, CategorySitemap

sitemaps = {
    'posts': PostSitemap,
    'authors': AutorSitemap,
    'categories': CategorySitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog', include('blog.urls', namespace='blog')),
    path('', include('catalog.urls', namespace='catalog')),
    path('', include('pages.urls', namespace='pages')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
