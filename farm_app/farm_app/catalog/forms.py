from django import forms

from farm_app.catalog.models import VegetableAndFruit, DairyProduct, AnimalProduct, Nut

labels = {
    'name': 'Name of product',
    'price': 'Price for 1 kg',
    'percent': 'Product percentage',
    'production': 'Country of production',
    'date_of_birth': 'Birthdate of the animal',
    'photo': 'Photo of product',
}


class VegetableCreationForm(forms.ModelForm):
    class Meta:
        model = VegetableAndFruit
        fields = ('name', 'price', 'photo','production')
        labels = labels


class DairyCreationForm(forms.ModelForm):
    class Meta:
        model = DairyProduct
        fields = ('name', 'percent', 'price', 'photo')
        labels = labels


class AnimalCreationForm(forms.ModelForm):
    class Meta:
        model = AnimalProduct
        fields = ('type', 'name', 'price', 'date_of_birth', 'production', 'photo')
        labels = labels


class NutCreationForm(forms.ModelForm):
    class Meta:
        model = Nut
        fields = ('type', 'name', 'price', 'photo')
        labels = labels
