from django.contrib import sitemaps
from django.urls import reverse


class PagesSitemap(sitemaps.Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return ['pages:about',
                'pages:top_range_100',
                'pages:top_time_charge_100',
                ]

    def location(self, item):
        return reverse(item)