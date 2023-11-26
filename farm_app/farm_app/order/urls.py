from django.urls import path

from farm_app.order.views import start_order, MyOrders,OrderDetails

urlpatterns = [
    path('start_order/', start_order, name='start order'),
    path('my-orders/<int:pk>/', MyOrders.as_view(), name='my orders'),
    path('order-details/<int:pk>/', OrderDetails.as_view(), name="detail order"),
]