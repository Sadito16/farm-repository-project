from itertools import chain

from django.views import generic as views
from django.shortcuts import render

from farm_app.catalog.models import VegetableAndFruit, DairyProduct, Nut, AnimalProduct


class IndexView(views.ListView):
    template_name = 'main/home.html'
    def get_queryset(self):
        veg_fruit = VegetableAndFruit.objects.all()
        nuts = Nut.objects.all()
        animal_products = AnimalProduct.objects.all()
        dairies = DairyProduct.objects.all()
        return list(chain(veg_fruit,nuts,animal_products,dairies))
    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['veg_fruit'] = VegetableAndFruit.objects.all()
        context['dairies'] = DairyProduct.objects.all()
        context['nuts'] = Nut.objects.all()
        context['animal_products'] = AnimalProduct.objects.all()
        return context

