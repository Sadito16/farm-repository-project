from django.urls import path

from farm_app.catalog.views import IndexView

urlpatterns = (
    path('', IndexView.as_view(), name='home'),

)