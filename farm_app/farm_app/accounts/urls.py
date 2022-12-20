from django.urls import path

from farm_app.accounts.views import ProfileLoginView,ProfileRegisterView

urlpatterns = (
    path('login/', ProfileLoginView.as_view(), name='profile login'),
    path('register/', ProfileRegisterView.as_view(), name='profile create'),

    # path('create/', ProfileLoginView.as_view(), name='profile login'),
    # path('edit/', ProfileLoginView.as_view(), name='profile login'),
    # path('delete/', ProfileLoginView.as_view(), name='profile login'),

)