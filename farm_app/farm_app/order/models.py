from django.db import models
from django.contrib.auth.models import User

from farm_app.accounts.validators import validate_only_digit_value
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
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    zipcode = models.IntegerField()
    city = models.CharField(max_length=100)
    phone = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    paid = models.BooleanField(default=False)
    paid_amount = models.IntegerField(blank=True, null=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=ORDERED)

    class Meta:
        ordering = ('-created_at',)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    fruit = models.ForeignKey(VegetableAndFruit, related_name='VegetableAndFruit', on_delete=models.CASCADE,null=True,blank=True)
    dairy = models.ForeignKey(DairyProduct, related_name='DairyProduct', on_delete=models.CASCADE,null=True,blank=True)
    meat = models.ForeignKey(AnimalProduct, related_name='AnimalProduct', on_delete=models.CASCADE,null=True,blank=True)
    nut = models.ForeignKey(Nut, related_name='Nut', on_delete=models.CASCADE,null=True,blank=True)


    price = models.IntegerField()
    quantity = models.IntegerField(default=1)

    def get_total_price(self):
        return f'${(self.price * self.quantity):.2f}'

    def get_name(self):
        if self.fruit:
            return f'{self.fruit.name}'
        elif self.dairy:
            return f'{self.dairy.name} {self.dairy.percent}%'
        if self.meat:
            return f'{self.meat.name} {self.meat.type}'
        if self.nut:
            return f'{self.nut.type} {self.nut.name}'


