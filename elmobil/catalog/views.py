import os

from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from .constants import MAX_OBJ_ON_PAGE
from .models import Car, Manufacturer


class CarsListView(ListView):
    model = Car
    paginate_by = MAX_OBJ_ON_PAGE
    paginate_orphans = 5
    ordering = 'title'

    def get_queryset(self):
        return self.model.objects.select_related(
            'manufacturer',
            'performance',
        ).order_by('title')


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
                'dimensions_weight',
                'charging_fast__type_port',
                'charging_fast__port_location__location',
                'charging_fast__port_location_2__location',
                'charging_fast__port_location__side',
                'charging_fast__port_location_2__side',
                'charging_fast__type_electric',
                'charging__type_port',
                'charging__port_location__location',
                'charging__port_location_2__location',
                'charging__port_location__side',
                'charging__port_location_2__side',
                'charging__type_electric',
                'miscellaneous__platform',
                'miscellaneous__car_body',
                'miscellaneous__segment',

            ),
            pk=self.kwargs['pk']
        )
        # car.increase_view_count() #  счетчик просмотров
        return car

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #  добавляем изображения из папки static/catalog/<car_id>
        img_list = []
        try:
            files = os.listdir(f'elmobil/static_dev/img/car_img/{self.object.pk}/')
            for file in files:
                if 'jpg' in file:
                    img_list.append(file)
        except FileNotFoundError:
            pass
        context['img_list'] = img_list  # список имен изображений
        # Добавляем формы
        return context


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
        ).order_by('title')

        paginator = Paginator(cars, MAX_OBJ_ON_PAGE)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        return context




