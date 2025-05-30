from urllib.parse import urlencode

from django.core.paginator import Paginator
from django.db.models import Prefetch, Q
from django.shortcuts import Http404, get_object_or_404, redirect
from django.urls import reverse
from django.utils.text import slugify
from django.views import View
from django.views.generic import DetailView, ListView

from catalog.constants import MAX_OBJ_ON_PAGE
from catalog.form import FilterForm
from catalog.models import Car, ImageCar, Manufacturer
from seo.mixins import SeoMixin


class CarsListView(SeoMixin, ListView):
    model = Car
    paginate_by = MAX_OBJ_ON_PAGE
    paginate_orphans = 5
    form_class = FilterForm

    def get_queryset(self):
        form = self.form_class(self.request.GET)
        if form.data:
            if form.is_valid():
                cleaned_data = {
                    key: value for key, value in form.cleaned_data.items() if value
                }
                return self._get_queryset(params=cleaned_data)
        return self._get_queryset()

    def _get_queryset(self, params: dict = None):
        queryset = (
            self.model.objects.select_related(
                "manufacturer",
                "performance",
                "performance__drive",
                "performance__acceleration_to_100",
            )
            .prefetch_related(
                Prefetch(
                    "images",
                    queryset=ImageCar.objects.only(
                        "image",
                        "name",
                    ),
                    to_attr="prefetched_images",
                )
            )
            .order_by("-year_release")
        )
        if params:
            queryset = queryset.filter(**params)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form_class
        return context


class CarDetailRedirectView(View):
    def get(self, request, pk):
        car = get_object_or_404(Car, pk=pk)
        return redirect("catalog:car_detail", pk=car.pk, slug=car.slug, permanent=True)


class CarDetailView(SeoMixin, DetailView):
    model = Car

    def get_object(self, queryset=None):
        car = get_object_or_404(
            Car.objects.select_related(
                "manufacturer",
                "real_range_estimation",
                "performance__acceleration_to_100",
                "performance__drive",
                "battery__battery_type",
                "battery__architecture",
                "battery__cathode",
                "battery__pack_configuration",
                "battery__nominal_voltage",
                "charging__type_port",
                "charging__type_electric",
                "charging_fast__type_port",
                "charging_fast__type_electric",
                "miscellaneous__platform",
                "miscellaneous__car_body",
                "miscellaneous__segment",
                "dimensions_weight",
            )
            .prefetch_related(
                "charging__port_location",
                "charging_fast__port_location",
                "images",
                "video_youtube",
            )
            .order_by("-year_release"),
            pk=self.kwargs["pk"],
        )
        # Храним просмотренные страницы в сессии
        self._increment_view_count(car)
        return car

    def _increment_view_count(self, car):
        """
        Увеличивает счетчик просмотров для указанного автомобиля.
        Примечания:
            Метод проверяет, была ли страница с автомобилем уже
            просмотрена в текущей сессии.
            Сохраняет просмотренные страницы в request.session
            Если нет, увеличивает счетчик просмотров автомобиля
            на 1 и сохраняет изменения в базе данных.
        """
        if f"viewed_page_{car.id}" not in self.request.session:
            self.request.session.setdefault(f"viewed_page_{car.id}", True)
            car.view_count += 1
            car.save()

    def get_meta_description(self):
        obj = self.object
        return f"Подробные характеристики {obj.title} года. Производителя {obj.manufacturer} "


class ManufacturerDetailView(SeoMixin, DetailView):
    model = Manufacturer
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cars = (
            Car.objects.select_related(
                "manufacturer",
                "performance",
                "performance__drive",
                "performance__acceleration_to_100",
            )
            .prefetch_related(
                Prefetch(
                    "images",
                    queryset=ImageCar.objects.only(
                        "image",
                        "name",
                    ),
                    to_attr="prefetched_images",
                )
            )
            .filter(manufacturer=self.object)
            .only(
                "id",
                "title",
                "manufacturer__title",
                "manufacturer__slug",
                "manufacturer__title",
                "year_release",
                "performance",
            )
            .order_by("-year_release")
        )
        paginator = Paginator(cars, MAX_OBJ_ON_PAGE)
        page_number = self.request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        if page_number and not page_obj.object_list:
            raise Http404("Страница не найдена")

        context["page_obj"] = page_obj
        return context

    def get_object(self, queryset=None):
        slug = self.kwargs["slug"]
        return get_object_or_404(Manufacturer, Q(slug=slug) | Q(slug=slugify(slug)))

    def get_meta_description(self):
        obj = self.object
        return f"{obj.title} - полный каталог электромобилей . Технические характеристики модельного ряда {obj.title}"


class ManufacturerTitleRedirect(View):
    def get(self, request, title):
        params = request.GET.dict()

        redirect_url = reverse("catalog:manufacturer", kwargs={"slug": slugify(title)})

        if params:
            redirect_url += "?" + urlencode(params)

        return redirect(redirect_url, permanent=True)
