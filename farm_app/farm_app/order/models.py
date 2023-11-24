from django.db import models
from django.contrib.auth.models import User
from farm_app.catalog.models import VegetableAndFruit, DairyProduct, Nut, AnimalProduct


UserModel = 'accounts.FarmerUser'

class Order(models.Model):
    ORDERED = 'ordered'
    SHIPPED = 'shipped'

    STATUS_CHOICES=(
        (ORDERED, 'Ordered'),
        (SHIPPED, 'Shipped')
    )

    user = models.ForeignKey(UserModel, related_name='orders', blank=True,null=True,
                             on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    paid = models.BooleanField(default=False)
    paid_amount = models.IntegerField(blank=True, null=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=ORDERED)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    fruit = models.ForeignKey(VegetableAndFruit, related_name='fruit', on_delete=models.CASCADE)
    dairy = models.ForeignKey(DairyProduct, related_name='dairy', on_delete=models.CASCADE)
    meat = models.ForeignKey(AnimalProduct, related_name='meat', on_delete=models.CASCADE)
    nut = models.ForeignKey(Nut, related_name='nut', on_delete=models.CASCADE)


    price = models.IntegerField()
    quantity = models.IntegerField(default=1)

