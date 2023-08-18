from django.apps import apps
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from farm_app.cart.cart import Cart
from json import JSONEncoder


def _default(self, obj):
    return getattr(obj.__class__, "to_json", _default.default)(obj)


_default.default = JSONEncoder().default
JSONEncoder.default = _default


@login_required(login_url='/login/')
def add_to_cart(request, item_type, product_id):
    cart = Cart(request)
    cart.add(product_id, item_type)
    cart.save()


    return render(request, 'cart/menu_cart.html')


def cart(request):
    return render(request, 'cart/cart.html')


def update_cart(request, product_id, action, item_type):
    print(f"item_type: {item_type}")
    cart = Cart(request)
    if action == 'increment':
        cart.add(product_id, item_type, 1, True)
    else:
        cart.add(product_id, item_type, quantity=-1, update_quantity=True)

    product_model = apps.get_model(app_label='catalog', model_name=item_type)
    product = product_model.objects.get(pk=product_id)
    quantity = cart.get_item(product_id)

    if quantity:
        quantity = quantity['quantity']

        item = {
            'product': {
                'id': product.id,
                'name': product.name,
                'photo': product.photo,
                'price': product.price,
            },
            'total_price': (quantity * product.price),
            'quantity': quantity,
        }
    else:
        item = None

    context = {
        'item': item,
        'total_cart_price': cart.get_total_cost,
    }
    response = render(request, 'cart/cart_item.html', context)
    response['HX-Trigger'] = 'update-menu-cart'

    return response


@login_required
def checkout(request):
    return render(request, 'cart/checkout.html')


def menu_cart(request):
    return render(request, 'cart/menu_cart.html')


def cart_total(request):
    return render(request, 'cart/cart_total.html')
