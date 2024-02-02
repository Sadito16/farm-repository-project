from django.apps import apps
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.views import generic as views
from django.shortcuts import render, redirect, get_object_or_404

from farm_app.cart.cart import Cart
from farm_app.order.models import Order, OrderItem

UserModel = get_user_model()

# @login_required
def start_order(request):
    cart = Cart(request)

    if request.method == "POST":
        print(request.POST.get('address'))
        user = request.user
        first_name = user.first_name
        last_name = user.last_name
        email = user.email
        address = request.POST.get('address')
        zipcode = request.POST.get('zipcode')
        city = request.POST.get('city')
        phone = request.POST.get('phone')

        order = Order.objects.create(user=user, first_name=first_name, last_name=last_name,
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

            cart.clear()

            return redirect('profile details', request.user.id)

        return redirect('cart')


class MyOrders(views.ListView):
    model = Order
    template_name = 'orders/my_orders.html'
    context_object_name = 'order'

    def model_name(self, product):
        return str(product.__class__.__name__)

    def get_queryset(self):
        user = get_object_or_404(UserModel, pk=self.kwargs['pk'])
        return Order.objects.filter(user=user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orders = self.get_queryset()

        # Calculate total price for each order and add it to the context
        total_prices = []
        for order in orders:
            total_price_of_order = order.items.aggregate(total=Sum('price'))['total']
            total_prices.append(total_price_of_order if total_price_of_order else 0)

        context = {
            'order_total_prices': total_prices,

        }


        return context

def order_details(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order_items = order.items.all()
    order_total = 0


    for item in order_items:
        order_total += item.price
    context = {
        'order': order,
        'order_items': order_items.count(),
        'order_total' : order_total,
    }

    return render(request, 'orders/order_details.html', context)