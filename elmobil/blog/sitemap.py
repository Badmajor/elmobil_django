from django.contrib import sitemaps
from .models import Post


class PostSitemap(sitemaps.Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Post.objects.order_by('-date_of_create')

    def lastmod(self, obj):
        return obj.date_of_change
