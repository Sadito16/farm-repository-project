from django.contrib.auth import models as auth_models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models

from farm_app.accounts.managers import FarmerUserManager


class FarmerUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    USERNAME_MAX_LENGTH = 30
    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        unique=True,
    )
    is_staff = models.BooleanField(
        default=False,
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    USERNAME_FIELD = 'username'

    objects = FarmerUserManager()


class Profile(models.Model):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 25
    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 25

    VEG_FRUT = 'Vegetables or Fruits'
    DAIRY = 'Dairy products'
    ANIMAL = 'Animal products'
    NUTS = 'Nuts'

    PRODUCTION_VARIETY = [(production, production) for production in (VEG_FRUT, DAIRY, ANIMAL, NUTS)]

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
        ),
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
        ),
    )

    image = models.FileField()

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    email = models.EmailField(
        null=True,
        blank=True,
    )

    production = models.CharField(
        max_length=max(len(production) for (production, _) in PRODUCTION_VARIETY),
        choices=PRODUCTION_VARIETY,
        null=True,
        blank=True,
        default=VEG_FRUT,
    )

    user = models.OneToOneField(
        FarmerUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


