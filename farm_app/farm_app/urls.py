
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/accounts', include('farm_app.accounts.urls')),
    path('', include('farm_app.main.urls')),
]
