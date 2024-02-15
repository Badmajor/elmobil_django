from django.contrib import sitemaps
from .models import Car, Manufacturer


class CarsSitemap(sitemaps.Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Car.objects.order_by('title')



class ManufacturersSitemap(sitemaps.Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Manufacturer.objects.order_by('title')