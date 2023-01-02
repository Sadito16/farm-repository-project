from django.views import generic as views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from farm_app.accounts.forms import CreateProfileForm, LoginProfileForm
from farm_app.accounts.models import Profile
from farm_app.catalog.models import VegetableAndFruit, DairyProduct, Nuts, AnimalProduct
from farm_app.common.mixins import RedirectToHome


class ProfileLoginView(auth_views.LoginView):
    form_class = LoginProfileForm
    template_name = 'accounts/profile_login.html'
    success_url = reverse_lazy('home')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class ProfileRegisterView(RedirectToHome, views.CreateView):
    form_class = CreateProfileForm
    template_name = 'accounts/profile_create.html'
    success_url = reverse_lazy('home')


class ProfileEditView(views.UpdateView):
    pass


#
# class DeleteProfileView(views.DeleteView):
#     pass
#
#
# class ChangeUserPasswordView(auth_views.PasswordChangeView):
#     template_name = 'accounts/change_password.html'
#
#
class ProfileDetailsView(views.DetailView):
    model = Profile
    template_name = 'accounts/profile_details.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if Profile.production == Profile.VEG_FRUT:
            production = list(VegetableAndFruit.objects.filter(user_id=self.object.user.id))

        elif Profile.production == Profile.DAIRY:
            production = list(DairyProduct.objects.filter(user_id=self.object.user.id))

        elif Profile.production == Profile.ANIMAL:
            production = list(AnimalProduct.objects.filter(user_id=self.object.user.id))

        else:

            production = list(Nuts.objects.filter(user_id=self.object.user.id))

        total_likes_count = sum(prod.likes for prod in production)
        total_pet_photos_count = len(production)

        context.update({
            'total_likes_count': total_likes_count,
            'total_images_count': total_pet_photos_count,
            'is_owner': self.object.user_id == self.request.user.id,
            'production': production,
        })
        return context
