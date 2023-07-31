from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from farm_app import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('farm_app.accounts.urls')),
    path('', include('farm_app.catalog.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
