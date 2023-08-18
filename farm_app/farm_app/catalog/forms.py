from django import forms
from django.forms import ImageField

from farm_app.catalog.models import VegetableAndFruit, DairyProduct, AnimalProduct, Nut

labels = {
    'name': 'Name of the product',
    'price': 'Price for 1 kg',
    'percent': 'Product percentage',
    'production': 'Country of production',
    'date_of_birth': 'Birthdate of the animal',
    'photo': 'Photo of the product',
}


class VegetableCreationForm(forms.ModelForm):
    class Meta:
        model = VegetableAndFruit
        fields = ('name', 'price', 'photo', 'production')
        widgets = {
            'name': forms.Select(attrs={'class': 'form-field'}),
            'price': forms.NumberInput(attrs={'class': 'form-field'}),
            'production': forms.TextInput(attrs={'class': 'form-field'}),
        }
        labels = labels


class DairyCreationForm(forms.ModelForm):
    class Meta:
        model = DairyProduct
        fields = ('name', 'percent', 'price','photo')
        labels = labels
        widgets = {
            'name': forms.Select(attrs={'class': 'form-field'}),
            'percent': forms.NumberInput(attrs={'class': 'form-field'}),
            'price': forms.NumberInput(attrs={'class': 'form-field'}),
        }


class AnimalCreationForm(forms.ModelForm):
    class Meta:
        model = AnimalProduct
        fields = ('type', 'name', 'price' ,'photo', 'date_of_birth', 'production')
        labels = labels
        widgets = {
            'type': forms.Select(attrs={'class': 'form-field'}),
            'name': forms.TextInput(attrs={'class': 'form-field'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-field'}),
            'price': forms.NumberInput(attrs={'class': 'form-field'}),
            'production': forms.TextInput(attrs={'class': 'form-field'}),
        }


class NutCreationForm(forms.ModelForm):
    class Meta:
        model = Nut
        fields = ('type', 'name', 'price','photo')
        widgets = {
            'type': forms.Select(attrs={'class': 'form-field'}),
            'name': forms.TextInput(attrs={'class': 'form-field'}),
            'price': forms.NumberInput(attrs={'class': 'form-field'}),

        }
