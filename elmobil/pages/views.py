from django.db import models
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView

from catalog.models import Car
from seo.mixins import SeoMixin


def about(request):
    template = "pages/about.html"
    context = dict(
        SITE_NAME="elmobil.ru",
        TITLE_FROM_INDEX="Электромобили: преимущества, "
        "технологии и перспективы развития",
    )
    return render(request, template, context)


class BaseTopListView(SeoMixin, ListView):
    model = Car
    paginate_by = 100
    paginate_orphans = 5
    template_name = "pages/top_list.html"
    title_page = None
    working_field = None
    measure = None
    url_name = None

    def get_queryset(self):
        queryset = self.model.objects.select_related(
            "manufacturer",
            self.get_parent_field(),
        ).order_by("-" + self.working_field)
        # Получаем максимальный запас хода
        max_value = queryset.aggregate(max_value=models.Max(self.working_field))[
            "max_value"
        ]
        # Добавляем процент от максимального значения в queryset
        queryset = queryset.annotate(
            measure=models.Value(self.measure, output_field=models.TextField()),
            value=models.F(self.working_field),
            percent=models.ExpressionWrapper(
                models.F("value") * 100 / max_value, output_field=models.FloatField()
            ),
        )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title_page"] = self.title_page
        context["measure"] = self.measure
        context["working_field"] = self.working_field
        context["url_page"] = reverse(f"pages:{self.url_name}")
        return context

    def get_parent_field(self):
        if not self.working_field:
            raise ValueError('Field: "working_field" is not filled')
        parent_field = self.working_field.split("__")[0]
        return parent_field


class TopRangeListView(BaseTopListView):
    working_field = "performance__electric_range"
    title_page = "Топ 100 Электромобилей по запасу хода"
    measure = "км"
    url_name = "top_range_100"
    meta_description = "Рейтинг электромобилей по запасу хода. Сравнение 100 лучших моделей с максимальным пробегом на одном заряде."


class TopChargeTimeListView(BaseTopListView):
    working_field = "charging__charge_speed"
    title_page = "Топ 100 Электромобилей по скорости зарядки"
    measure = "км в час"
    url_name = "top_time_charge_100"
    meta_description = "Рейтинг электромобилей по скорости зарядки. Сравнение 100 лучших моделей с максимальной скоростью зарядки."
