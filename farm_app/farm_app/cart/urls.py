from django.urls import path

from farm_app.cart.views import add_to_cart, cart, checkout, menu_cart, update_cart, cart_total

urlpatterns = [
    path('', cart, name='cart'),
    path('add/<str:item_type>/<int:product_id>/', add_to_cart, name='add to cart'),
    path('checkout/', checkout, name='checkout'),
    path('menu-cart/', menu_cart, name='menu cart'),
    path('total/', cart_total, name='cart total'),
    path('update_cart/<int:product_id>/<str:action>/<str:item_type>/', update_cart, name='update cart'),
]
