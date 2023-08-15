from itertools import chain

from django.core.serializers.json import DjangoJSONEncoder
from django.conf.urls.static import static
from django.urls import reverse, reverse_lazy
from django.views import generic as views
import json

from farm_app.accounts.models import FarmerUser
from farm_app.catalog.forms import *
from farm_app.catalog.models import *
from farm_app.catalog.serializers import VegetableAndFruitSerializer, DairyProductSerializer, NutSerializer, \
    AnimalProductSerializer


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

        context['users'] = FarmerUser.objects.all()
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
        self.object.user_id = self.request.user.pk
        self.object.save()
        return super().form_valid(form)


class VegetableEditView(views.UpdateView):
    model = VegetableAndFruit
    template_name = 'catalog/edit-vegetable-page.html'
    fields = ['name', 'price','production']
    context_object_name = 'plant'
    def get_success_url(self):
        return reverse('details vegetable', kwargs={
            'pk': self.object.pk,
        })

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class VegetableDetailsView(views.DetailView):
    model = VegetableAndFruit
    context_object_name = 'plant'
    template_name = 'catalog/details-vegetable-page.html'
    photo = static('images/fruit-and-veg.jpg')
    model_name = object.__class__.__name__

    def get_photo(self):
        if self.object.photo is not None:
            return self.object.photo
        return self.photo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'photo': self.get_photo,
            'model_name': self.model_name,
        })

        return context




class VegetableDeleteView(views.DeleteView):
    model = VegetableAndFruit
    context_object_name = 'product'
    template_name = 'catalog/delete-page.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


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


class NutEditView(views.UpdateView):
    model = Nut
    template_name = 'catalog/edit-nut-page.html'
    fields = ['type','name', 'price','package']
    context_object_name = 'nut'

    def get_success_url(self):
        return reverse('details nut', kwargs={
            'pk': self.object.pk,
        })

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class NutDetailsView(views.DetailView):
    model = Nut
    context_object_name = 'nut'
    template_name = 'catalog/details-nut-page.html'
    photo = static('images/nuts-and-dry-fruits.jpg')
    model_name = object.__class__.__name__

    def get_photo(self):
        if self.object.photo is not None:
            return self.object.photo
        return self.photo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'photo': self.get_photo,
            'model_name': self.model_name,
        })

        return context



class NutDeleteView(views.DeleteView):
    model = Nut
    context_object_name = 'product'
    template_name = 'catalog/delete-page.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


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


class DairyEditView(views.UpdateView):
    model = DairyProduct
    template_name = 'catalog/edit-dairy-page.html'
    fields = ['name','percent', 'price']
    context_object_name = 'dairy'

    def get_success_url(self):
        return reverse('details dairy', kwargs={
            'pk': self.object.pk,
        })

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class DairyDetailsView(views.DetailView):
    model = DairyProduct
    context_object_name = 'dairy'
    template_name = 'catalog/details-dairy-page.html'
    photo = static('images/milk-products.jpg')
    model_name = object.__class__.__name__

    def get_photo(self):
        if self.object.photo is not None:
            return self.object.photo
        return self.photo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'photo': self.get_photo,
            'model_name': self.model_name,
        })

        return context



class DairyDeleteView(views.DeleteView):
    model = Nut
    context_object_name = 'product'
    template_name = 'catalog/delete-page.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


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


class AnimalEditView(views.UpdateView):
    model = AnimalProduct
    template_name = 'catalog/edit-animal-page.html'
    fields = ['type','name', 'price', 'production']
    context_object_name = 'animal'

    def get_success_url(self):
        return reverse('details animal', kwargs={
            'pk': self.object.pk,
        })

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AnimalDetailsView(views.DetailView):
    model = AnimalProduct
    context_object_name = 'meat'
    template_name = 'catalog/details-animal-page.html'
    photo = static('images/meat.jpg')
    model_name = object.__class__.__name__

    def get_photo(self):
        if self.object.photo is not None:
            return self.object.photo
        return self.photo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'photo': self.get_photo,
            'model_name': self.model_name,
        })

        return context



class AnimalDeleteView(views.DeleteView):
    model = AnimalProduct
    context_object_name = 'product'
    template_name = 'catalog/delete-page.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
