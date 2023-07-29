from django.contrib import admin

# Register your models here.
from farm_app.catalog.models import VegetableAndFruit, DairyProduct, AnimalProduct, Nut


@admin.register(VegetableAndFruit)
class VegetableAndFruitAdmin(admin.ModelAdmin):
    pass

@admin.register(DairyProduct)
class DairyProductAdmin(admin.ModelAdmin):
    pass
@admin.register(AnimalProduct)
class AnimalProductAdmin(admin.ModelAdmin):
    pass
@admin.register(Nut)
class Nut(admin.ModelAdmin):
    pass
