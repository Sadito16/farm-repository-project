from itertools import chain

from django.forms import formset_factory
from django.urls import reverse
from django.views import generic as views

from farm_app.catalog.forms import *
from farm_app.catalog.models import *


class IndexView(views.ListView):
    template_name = 'main/home.html'

    def get_queryset(self):
        veg_fruit = VegetableAndFruit.objects.all()
        nuts = Nut.objects.all()
        animal_products = AnimalProduct.objects.all()
        dairies = DairyProduct.objects.all()
        return list(chain(veg_fruit, nuts, animal_products, dairies))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['veg_fruit'] = VegetableAndFruit.objects.all()
        context['dairies'] = DairyProduct.objects.all()
        context['nuts'] = Nut.objects.all()
        context['animal_products'] = AnimalProduct.objects.all()
        return context


class VegetableCreateView(views.CreateView):
    template_name = 'catalog/create-vegetable-page.html'
    model = VegetableAndFruit
    form_class = VegetableCreationForm

    def get_success_url(self):
        return reverse('details vegetable', kwargs={
            'pk': self.object.pk,
        })

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user_id=self.request.user.pk
        self.object.save()
        return super().form_valid(form)


class VegetableEditView(views.DetailView):
    pass


class VegetableDetailsView(views.DetailView):
    pass


class VegetableDeleteView(views.DeleteView):
    pass


class NutCreateView(views.CreateView):
    template_name = 'catalog/create-nut-page.html'
    model = Nut
    form_class = NutCreationForm

    def get_success_url(self):
        return reverse('details nut', kwargs={
            'pk': self.object.pk,
        })

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user_id = self.request.user.pk
        self.object.save()
        return super().form_valid(form)


class NutEditView(views.DetailView):
    pass


class NutDetailsView(views.DetailView):
    pass


class NutDeleteView(views.DeleteView):
    pass


class DairyCreateView(views.FormView):
    template_name = 'catalog/create-dairy-page.html'
    model = DairyProduct
    form_class = DairyCreationForm

    def get_success_url(self):
        return reverse('details dairy', kwargs={
            'pk': self.object.pk,
        })

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user_id = self.request.user.pk
        self.object.save()
        return super().form_valid(form)


class DairyEditView(views.DetailView):
    pass


class DairyDetailsView(views.DetailView):
    pass


class DairyDeleteView(views.DeleteView):
    pass


class AnimalCreateView(views.FormView):
    template_name = 'catalog/create-animal-page.html'
    model = AnimalProduct
    form_class = AnimalCreationForm

    def get_success_url(self):
        return reverse('details animal', kwargs={
            'pk': self.object.pk,
        })

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user_id = self.request.user.pk
        self.object.save()
        return super().form_valid(form)


class AnimalEditView(views.DetailView):
    pass


class AnimalDetailsView(views.DetailView):


class AnimalDeleteView(views.DeleteView):
    pass
