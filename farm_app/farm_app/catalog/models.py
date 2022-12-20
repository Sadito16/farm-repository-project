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
