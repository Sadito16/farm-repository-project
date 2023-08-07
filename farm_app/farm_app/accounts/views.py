from django.conf.urls.static import static
from django.views import generic as views
from django.contrib.auth import views as auth_views, login, get_user_model
from django.urls import reverse_lazy, reverse

from farm_app.accounts.forms import CreateProfileForm, LoginProfileForm
from farm_app.accounts.models import FarmerUser
from farm_app.catalog.models import VegetableAndFruit, DairyProduct, Nut, AnimalProduct

UserModel = get_user_model()

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
    picture = static('images/profile.jpg')

    def get_profile_image(self):
        if self.object.profile_picture is not None:
            return self.object.profile_picture
        return self.picture


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['veg_fruit'] = VegetableAndFruit.objects.filter(user_id=user.id)
        context['dairies'] = DairyProduct.objects.filter(user_id=user.id)
        context['nuts'] = Nut.objects.filter(user_id=user.id)
        context['animal_products'] = AnimalProduct.objects.filter(user_id=user.id)
        context['profile_picture'] = self.get_profile_image()
        context['products_count'] = (VegetableAndFruit.objects.all().filter(user_id=user.id).count()
                                     + DairyProduct.objects.all().filter(user_id=user.id).count()
                                     + Nut.objects.all().filter(user_id=user.id).count()
                                     + AnimalProduct.objects.all().filter(user_id=user.id).count())
        return context


class ProfileEditView(views.UpdateView):
    model = UserModel
    template_name = 'accounts/profile_edit.html'
    fields = ['username','first_name','last_name','email','date_of_birth','gender']

    def get_success_url(self):
        return reverse('profile details', kwargs={
            'pk': self.object.pk,
        })

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ProfileDeleteView(views.DeleteView):
    model = FarmerUser
    template_name = 'accounts/profile_delete.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context