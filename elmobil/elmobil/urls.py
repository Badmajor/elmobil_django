from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

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
    path('api/', include('api.urls')),
    path('', include('catalog.urls', namespace='catalog')),
    path('', include('pages.urls', namespace='pages')),
    path(r'auth/', include('djoser.urls')),
    path(r'auth/', include('djoser.urls.jwt')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', TemplateView.as_view(
        template_name="robots.txt",
        content_type="text/plain"
    )),
]

handler404 = "elmobil.views.page_not_found_view"

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

schema_view = get_schema_view(
    openapi.Info(
        title="Elmobil API",
        default_version='v1',
        description="Документация для приложения elmobil",
        contact=openapi.Contact(email="v.balonkin@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0),
            name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0),
            name='schema-redoc'),
]
