from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from .constants import MAX_OBJ_ON_PAGE
from .form import FilterForm
from .models import Car, Manufacturer


class CarsListView(ListView):
    model = Car
    paginate_by = MAX_OBJ_ON_PAGE
    paginate_orphans = 5
    form_class = FilterForm

    def get_queryset(self):
        form = self.form_class(self.request.GET)
        if form.data:
            if form.is_valid():
                cleaned_data = {key: value
                                for key, value in form.cleaned_data.items()
                                if value}
                return self._get_queryset(params=cleaned_data)
        return self._get_queryset()

    def _get_queryset(self, params: dict = None):
        queryset = self.model.objects.select_related(
            'manufacturer',
            'real_range_estimation',
            'performance__acceleration_to_100',
            'performance__drive',
            'miscellaneous__car_body'
        ).prefetch_related(
            'charging__port_location',
            'charging_fast__port_location',
            'images',
            'video_youtube'
        ).order_by('-year_release')
        if params:
            queryset = queryset.filter(**params)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class
        return context


class CarDetailView(DetailView):
    model = Car

    def get_object(self, queryset=None):
        car = get_object_or_404(
            Car.objects.select_related(
                'manufacturer',
                'real_range_estimation',
                'performance__acceleration_to_100',
                'performance__drive',
                'battery__battery_type',
                'battery__architecture',
                'battery__cathode',
                'battery__pack_configuration',
                'battery__nominal_voltage',
                'charging__type_port',
                'charging__type_electric',
                'charging_fast__type_port',
                'charging_fast__type_electric',
                'miscellaneous__platform',
                'miscellaneous__car_body',
                'miscellaneous__segment',
                'dimensions_weight',
            ).prefetch_related(
                'charging__port_location',
                'charging_fast__port_location',
                'images',
                'video_youtube'
            ).order_by('-year_release'),
            pk=self.kwargs['pk']
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
        if f'viewed_page_{car.id}' not in self.request.session:
            self.request.session.setdefault(f'viewed_page_{car.id}', True)
            car.view_count += 1
            car.save()


class ManufacturerDetailView(DetailView):
    model = Manufacturer
    slug_field = 'title'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get cars this manufacturer
        cars = Car.objects.select_related(
            'manufacturer',
            'performance',
        ).filter(
            manufacturer=self.object
        ).order_by('-year_release')

        paginator = Paginator(cars, MAX_OBJ_ON_PAGE)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        return context
