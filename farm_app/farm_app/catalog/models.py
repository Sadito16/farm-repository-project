import datetime
from enum import Enum

from django.contrib.auth import get_user_model
from django.db import models

UserModel = 'accounts.FarmerUser'


class ChoicesMixin:
    @classmethod
    def choice(cls):
        return [(choice.value, choice.name) for choice in cls]


class ChoicesLengthMixin(ChoicesMixin):
    @classmethod
    def max_length(cls):
        return max(len(ch.value) for ch in cls)


class VegFruitChoice(ChoicesLengthMixin, Enum):
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

class DairyChoice(ChoicesLengthMixin, Enum):
    MILK = 'Milk'
    BUTTER = 'Butter'
    CHEESE = 'Cheese'
    CURD = 'Curd'
    YOGURT = 'Yogurt'
    OTHER = 'Other'


class AnimalChoice(ChoicesLengthMixin,Enum):
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

class NutChoices(ChoicesLengthMixin,Enum):
    ROASTED = 'Roasted'
    RAW = 'Row'
    DRIED_FRUIT = 'Dried'
    OTHER = 'Other'
class VegetableAndFruit(models.Model):


    name = models.CharField(choices=VegFruitChoice.choice(),
                              max_length=VegFruitChoice.max_length(),
                              default=VegFruitChoice.OTHER.value)

    price = models.FloatField()

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
    publication_date = models.DateField(
        auto_now=True,
    )


    def __str__(self):
        return f'{self.name}'

    class Meta:
        unique_together = ('user', 'name')


class DairyProduct(models.Model):

    name = models.CharField(choices=DairyChoice.choice(),
                              max_length=DairyChoice.max_length(),
                              default=DairyChoice.OTHER.value)
    percent = models.FloatField(null=True,blank=True)
    price = models.FloatField()

    publication_date = models.DateField(
        auto_now=True,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
    class Meta:
        unique_together = ('user', 'name')

    def __str__(self):
        if self.percent:
            return f'{self.percent}% {self.name}'
        return f'{self.name}'



class AnimalProduct(models.Model):

    PRODUCT_MAX_LENGTH = 40

    type = models.CharField(choices=AnimalChoice.choice(),
                              max_length=AnimalChoice.max_length(),
                              default=AnimalChoice.OTHER.value)
    name = models.CharField(
        max_length=PRODUCT_MAX_LENGTH,
    )
    price = models.FloatField()

    date_of_birth = models.DateField(
        null=True,
        blank=True,
        unique=True,)
    publication_date = models.DateField(
        auto_now=True,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    @property
    def age(self):
        return datetime.datetime.now().year - self.date_of_birth.year

    def __str__(self):
        return f'{self.name} from {self.type}'


class Nut(models.Model):
    NUTS_MAX_LENGTH = 35

    type = models.CharField(choices=NutChoices.choice(),
                              max_length=NutChoices.max_length(),
                              default=NutChoices.OTHER.value)

    name = models.CharField(
        max_length=NUTS_MAX_LENGTH,
    )
    price = models.FloatField()
    package = models.IntegerField()
    publication_date = models.DateField(
        auto_now=True,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.type} {self.name}'

