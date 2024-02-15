from django.contrib import sitemaps
from .models import Post, Category, Autor


class PostSitemap(sitemaps.Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.updated_at


class CategorySitemap(sitemaps.Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Category.objects.all()

    def lastmod(self, obj):
        return obj.updated_at


class AutorSitemap(sitemaps.Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Autor.objects.all()

    def lastmod(self, obj):
        return obj.updated_at