from django.db import models
from django.shortcuts import render
from django.views.generic import ListView

from catalog.models import Car, Manufacturer


def about(request):
    template = 'pages/about.html'
    context = dict(
        SITE_NAME='elmobil.ru',
        TITLE_FROM_INDEX='Электромобили: преимущества, технологии и перспективы развития'
    )
    return render(request, template, context)


class TopRangeListView(ListView):
    model = Car
    paginate_by = 100
    paginate_orphans = 5
    template_name = 'pages/car_list.html'


    def get_queryset(self):
        queryset =  self.model.objects.select_related(
            'manufacturer',
            'performance',
        ).order_by('-performance__electric_range')
        # Добавляем процент от максимального значения в queryset
        queryset = queryset.annotate(
            recent_to_max_range=models.ExpressionWrapper(
                models.F('performance__electric_range') * 100 / models.Max('performance__electric_range'),
                output_field=models.FloatField()
            )
        )

        return queryset


