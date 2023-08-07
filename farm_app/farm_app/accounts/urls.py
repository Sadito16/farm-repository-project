from django.urls import path, include

from farm_app.accounts.views import ProfileLoginView, ProfileRegisterView, ProfileDetailsView, ProfileLogoutView, \
    ProfileEditView, ProfileDeleteView

urlpatterns = (
    path('login/', ProfileLoginView.as_view(), name='login'),
    path('register/', ProfileRegisterView.as_view(), name='register'),
    path('logout/',ProfileLogoutView.as_view(), name='logout'),

    path('<int:pk>/',include([
        path('', ProfileDetailsView.as_view(), name='profile details'),
        path('edit/', ProfileEditView.as_view(), name='profile edit'),
        path('delete/', ProfileDeleteView.as_view(), name='profile delete'),
    ])),
)