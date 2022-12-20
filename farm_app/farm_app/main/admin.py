from django.contrib import admin

# Register your models here.
from farm_app.main.models import  VegetableAndFruit


@admin.register(VegetableAndFruit)
class VegetableAndFruitAdmin(admin.ModelAdmin):
    pass
