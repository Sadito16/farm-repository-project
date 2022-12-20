from django.contrib import admin

# Register your models here.
from farm_app.catalog.models import  VegetableAndFruit


@admin.register(VegetableAndFruit)
class VegetableAndFruitAdmin(admin.ModelAdmin):
    pass
