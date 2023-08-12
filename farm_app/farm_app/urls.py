from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from farm_app import settings
from farm_app.cart.views import add_to_cart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('farm_app.accounts.urls')),
    path('', include('farm_app.catalog.urls')),
    path('cart/', include('farm_app.cart.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
