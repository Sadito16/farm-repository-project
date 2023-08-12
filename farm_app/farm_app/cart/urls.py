from django.urls import path

from farm_app.cart.views import add_to_cart, cart, checkout, menu_cart, update_cart, cart_total

urlpatterns = [
    path('add/<int:product_id>', add_to_cart, name='add to cart'),
    path('', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('menu-cart/', menu_cart, name='menu cart'),
    path('cart-total/', cart_total, name='cart total'),
    path('update_cart/<int:product_id>/<str:action>/', update_cart, name='update cart'),
]
