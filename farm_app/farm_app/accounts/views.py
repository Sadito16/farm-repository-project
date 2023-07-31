from django.views import generic as views
from django.contrib.auth import views as auth_views, login
from django.urls import reverse_lazy

from farm_app.accounts.forms import CreateProfileForm, LoginProfileForm
from farm_app.accounts.models import FarmerUser
from farm_app.catalog.models import VegetableAndFruit, DairyProduct, Nut, AnimalProduct


class ProfileLoginView(auth_views.LoginView):
    form_class = LoginProfileForm
    template_name = 'accounts/profile_login.html'

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        return form


class ProfileRegisterView(views.CreateView):
    model  = FarmerUser
    form_class = CreateProfileForm
    template_name = 'accounts/profile_create.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result

class ProfileLogoutView(auth_views.LogoutView):
    pass


class ProfileDetailsView(views.DetailView):
    model = FarmerUser
    template_name = 'accounts/profile_details.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['veg_fruit'] = VegetableAndFruit.objects.all()
        context['dairies'] = DairyProduct.objects.all()
        context['nuts'] = Nut.objects.all()
        context['animal_products'] = AnimalProduct.objects.all()
        return context