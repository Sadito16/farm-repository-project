from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from farm_app.accounts.models import FarmerUser
from farm_app.common.helpers import BootstrapFormMixin
from farm_app.catalog.models import VegetableAndFruit


class CreateProfileForm(auth_forms.UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={'class': 'create-field', 'type': 'password'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(
            attrs={'class': 'create-field', 'type': 'password'}),
    )
    class Meta(auth_forms.UserCreationForm.Meta):
        model = FarmerUser
        fields = ('first_name','last_name','username','email', 'password1', 'password2')

        widgets= {
            'first_name': forms.TextInput(attrs={'class':'create-field'}),
            'last_name': forms.TextInput(attrs={'class': 'create-field'}),
            'username': forms.TextInput(attrs={'class': 'create-field'}),
            'email': forms.EmailInput(attrs={'class': 'create-field'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

class LoginProfileForm(auth_forms.AuthenticationForm):
    username = auth_forms.UsernameField(
        widget=forms.TextInput(
            attrs={"autofocus": True,
                   "class": "login-field",}))
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password",
                   "class": "login-field",}),
    )


class EditProfileForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        # self.initial['production'] = Profile.VEG_FRUIT
        # self.initial['gender'] = Profile.DO_NOT_SHOW

    class Meta:
        model = FarmerUser
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter first name'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter last name'
                }
            ),
            'profile_picture': forms.TextInput(
                attrs={
                    'placeholder': 'Enter URL'
                }

            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Enter email'
                }
            ),

            'date_of_birth': forms.DateInput(
                attrs={
                    'min': '1920-01-01',
                }
            )
        }

#
# class DeleteProfileForm(forms.ModelForm):
#     def save(self, commit=True):
#         pets = list(self.instance.pet_set.all())
#         # should be done with signals
#         PetPhoto.objects.filter(tagged_pets__in=pets).delete()
#
#         self.instance.delete()
#         return self.instance
#
#     class Meta:
#         model = Profile
#         fields = ()
