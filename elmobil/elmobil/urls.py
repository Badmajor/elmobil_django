from django.conf import settings
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include

from blog.sitemap import PostSitemap
from catalog.sitemap import CarsSitemap, ManufacturersSitemap
from django.views.generic import TemplateView
from pages.sitemap import PagesSitemap

sitemaps = {
    'posts': PostSitemap,
    'cars': CarsSitemap,
    'manufacturers': ManufacturersSitemap,
    'pages': PagesSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
    path('', include('catalog.urls', namespace='catalog')),
    path('', include('pages.urls', namespace='pages')),
    path('api/', include('api.urls', namespace='api')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
]

handler404 = "elmobil.views.page_not_found_view"

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
