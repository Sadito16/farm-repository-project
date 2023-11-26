from django.views import generic as views
from django.shortcuts import render, redirect

from farm_app.cart.cart import Cart
from farm_app.order.models import Order, OrderItem


def start_order(request):
    cart = Cart(request)

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        zipcode = request.POST.get('zipcode')
        city = request.POST.get('city')
        phone = request.POST.get('phone')

        order = Order.objects.create(user=request.user, first_name=first_name, last_name=last_name,
                                     email=email, address=address, zipcode=zipcode, city=city, phone=phone)

        for item in cart:
            quantity = int(item['quantity'])

            if item['item_type'] == "VegetableAndFruit":
                fruit = item[item['item_type']]
                dairy = None
                meat = None
                nut = None
                price = fruit.price * quantity

            elif item['item_type'] == "DairyProduct":
                dairy = item[item['item_type']]
                fruit = None
                meat = None
                nut = None
                price = dairy.price * quantity

            elif item['item_type'] == "AnimalProduct":
                meat = item[item['item_type']]
                dairy = None
                fruit = None
                nut = None
                price = meat.price * quantity

            else:
                nut = item[item['item_type']]
                dairy = None
                meat = None
                fruit = None
                price = nut.price * quantity

            item = OrderItem.objects.create(order=order, fruit=fruit, meat=meat, dairy=dairy, nut=nut, price=price,
                                            quantity=quantity)

        return redirect('profile details', request.user.id)

    return redirect('cart')


class MyOrders(views.DetailView):
    model = Order
    template_name = 'orders/my_orders.html'
    context_object_name = 'order'

    def model_name(self, product):
        return str(product.__class__.__name__)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.get_object()

        context['user'] = user

        return context


class OrderDetails(views.DetailView):
    model = Order
    template_name = 'orders/order_details.html'
    context_object_name = 'order'


