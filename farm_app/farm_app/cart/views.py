from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from farm_app.cart.cart import Cart
from farm_app.catalog.models import VegetableAndFruit


def add_to_cart(request,product_id):
    cart = Cart(request)
    cart.add(product_id)
    cart.save()

    return render(request, 'cart/menu_cart.html')

def cart(request):
    return render(request, 'cart/cart.html')

def update_cart(request,product_id,action):
    cart = Cart(request)

    if action == 'increment':
        cart.add(product_id,1,True)
    else:
        cart.add(product_id, quantity=-1,update_quantity=True)

    vegetable = VegetableAndFruit.objects.get(pk=product_id)
    quantity = cart.get_item(product_id)

    if quantity:
        quantity = quantity['quantity']

        item = {
            'vegetable': {
                'id': vegetable.id,
                'name': vegetable.name,
                'photo': vegetable.photo,
                'price': vegetable.price,
            },
            'total_price': (quantity * vegetable.price),
            'quantity': quantity,
        }

    else:
        item = None



    response = render(request, 'cart/cart_item.html', {'item': item})
    response['HX-Trigger'] = 'update-menu-cart'

    return response

@login_required
def checkout(request):
    return render(request, 'cart/checkout.html')

def menu_cart(request):
    return render(request, 'cart/menu_cart.html')

def cart_total(request):
    return render(request, 'cart/cart_total.html')