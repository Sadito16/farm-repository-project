from django.urls import path

from farm_app.accounts.views import ProfileLoginView, ProfileRegisterView, ProfileEditView, ProfileDetailsView

urlpatterns = (
    path('login/', ProfileLoginView.as_view(), name='profile login'),
    path('register/', ProfileRegisterView.as_view(), name='profile create'),
    path('logout/',ProfileRegisterView.as_view(), name='profile logout'),

    path('<int:pk>/', ProfileDetailsView.as_view(), name='profile details'),
    path('edit/', ProfileEditView.as_view(), name='profile login'),
    # path('delete/', ProfileLoginView.as_view(), name='profile login'),

)