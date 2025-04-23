from django.contrib import sitemaps
from django.urls import reverse
from .models import Car, Manufacturer


class CarsSitemap(sitemaps.Sitemap):
    protocol = "https"
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Car.objects.order_by("title")

    def location(self, car):
        return reverse("catalog:car_detail", kwargs={"pk": car.pk, "slug": car.slug})


class ManufacturersSitemap(sitemaps.Sitemap):
    protocol = "https"
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Manufacturer.objects.order_by("title")
