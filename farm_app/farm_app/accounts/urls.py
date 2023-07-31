from django.urls import path

from farm_app.accounts.views import ProfileLoginView, ProfileRegisterView, ProfileDetailsView, ProfileLogoutView

urlpatterns = (
    path('login/', ProfileLoginView.as_view(), name='login'),
    path('register/', ProfileRegisterView.as_view(), name='register'),
    path('logout/',ProfileLogoutView.as_view(), name='logout'),

    path('<int:pk>/', ProfileDetailsView.as_view(), name='profile details'),
    # path('edit/', ProfileEditView.as_view(), name='profile login'),
    # path('delete/', ProfileLoginView.as_view(), name='profile login'),

)