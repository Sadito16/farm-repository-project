import datetime

from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class VegetableAndFruit(models.Model):
    CARROT = 'Carrot'
    POTATO = 'Potato'
    CABBAGE = 'Cabbage'
    CAULIFLOWER = 'Cauliflower'
    CUCUMBERS = 'Cucumber'
    TOMATO = 'Tomato'
    ONION = 'Onion'
    BROCCOLI = 'Broccoli'
    EGGPLANT = 'Eggplant'
    PEPPER = 'Pepper'
    CORN = 'Corn'
    PUMPKIN = 'Pumpkin'
    APPLE = 'Apple'
    GRAPE = 'Grape'
    STRAWBERRY = 'Strawberry'
    PEAR = 'Pear'
    PLUM = 'Plum'
    ORANGE = 'Orange'
    CHERRY = 'Cherry'
    BLACKBERRY = 'Blackberry'
    LEMON = 'Lemon'
    PEACH = 'Peach'
    MELON = 'Melon'
    WATERMELON = 'Watermelon'
    OTHER = 'Other'

    PLANT_CHOICES = [(x, x) for x in (ORANGE, OTHER, WATERMELON, MELON, PEACH, LEMON, BLACKBERRY,
                                      CHERRY, PLUM, PEAR, STRAWBERRY, GRAPE, CARROT,
                                      APPLE, PUMPKIN, CORN, PEPPER, EGGPLANT, BROCCOLI,
                                      ONION, TOMATO, CUCUMBERS, CAULIFLOWER, CABBAGE, POTATO)]

    name = models.CharField(
        max_length=max(len(x) for (x, _) in PLANT_CHOICES),
        choices=PLANT_CHOICES,
        default=OTHER,
    )

    price = models.IntegerField()

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.name} - {self.price} lv.'

    class Meta:
        unique_together = ('user', 'name')


class DairyProduct(models.Model):
    MILK = 'Milk'
    BUTTER = 'Butter'
    CHEESE = 'Cheese'
    CURD = 'Curd'
    YOGURT = 'Yogurt'
    OTHER = 'Other'

    DAIRY_CHOICES = [(x, x) for x in (BUTTER, CHEESE, CURD, MILK, YOGURT, OTHER)]

    name = models.CharField(
        max_length=max(len(x) for (x, _) in DAIRY_CHOICES),
        choices=DAIRY_CHOICES,
        default=OTHER,
    )
    percent = models.IntegerField()
    price = models.IntegerField()

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.name} - {self.price} lv.'

    class Meta:
        unique_together = ('user', 'name')


class AnimalProduct(models.Model):
    CHICKEN = 'Chicken'
    PIG = 'Pig'
    COW = 'Cow'
    GOAT = 'Goat'
    SHEEP = 'Sheep'
    TURKEY = 'Turkey'
    GOOSE = 'Goose'
    RABBIT = 'Rabbit'
    HORSE = 'Horse'
    DONKEY = 'Donkey'
    LAMB = 'Lamb'
    OTHER = 'Other'

    ANIMAL_CHOICES = [(x, x) for x in
                      (CHICKEN, COW, HORSE, DONKEY, GOAT, GOOSE, LAMB, PIG, RABBIT, SHEEP, TURKEY, OTHER)]

    PRODUCT_MAX_LENGTH = 40

    type = models.CharField(
        max_length=max(len(x) for (x, _) in ANIMAL_CHOICES),
        choices=ANIMAL_CHOICES,
        default=OTHER,
    )
    name = models.CharField(
        max_length=PRODUCT_MAX_LENGTH,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
        unique=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    @property
    def age(self):
        return datetime.datetime.now().year - self.date_of_birth.year

    def __str__(self):
        return f'{self.name} the {self.type}'

class Nuts(models.Model):
    NUTS_MAX_LENGTH = 35

    ROASTED = 'Roasted'
    RAW = 'Row'
    DRIED_FRUIT = 'Dried fruit'
    SEEDS = 'Seeds'
    OTHER = 'Other'

    NUTS_CHOICES = [(x, x) for x in (DRIED_FRUIT,ROASTED,RAW,SEEDS,OTHER)]

    type = models.CharField(
        max_length=max(len(x) for (x, _) in NUTS_CHOICES),
        choices=NUTS_CHOICES,
        default=OTHER,
    )
    name = models.CharField(
        max_length=NUTS_MAX_LENGTH,
    )
    package = models.IntegerField()
