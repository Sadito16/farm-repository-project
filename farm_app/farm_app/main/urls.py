from django.urls import path

from farm_app.main.views import IndexView

urlpatterns = (
    path('', IndexView.as_view()),
)