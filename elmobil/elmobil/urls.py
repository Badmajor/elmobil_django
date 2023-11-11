from django.conf import settings
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog', include('blog.urls', namespace='blog')),
    path('', include('catalog.urls', namespace='catalog')),
    path('about/', include('pages.urls', namespace='pages')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
