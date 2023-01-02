from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from farm_app.accounts.models import Profile
from farm_app.common.helpers import BootstrapFormMixin
from farm_app.catalog.models import VegetableAndFruit


class CreateProfileForm(BootstrapFormMixin, auth_forms.UserCreationForm):
    first_name = forms.CharField(
        max_length=Profile.FIRST_NAME_MAX_LENGTH,
    )

    last_name = forms.CharField(
        max_length=Profile.LAST_NAME_MAX_LENGTH,
    )

    image = forms.URLField()

    date_of_birth = forms.DateField()

    email = forms.EmailField()

    production = forms.ChoiceField(
        choices=Profile.PRODUCTION_VARIETY,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        user = super().save(commit=commit)
        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            picture=self.cleaned_data['picture'],
            date_of_birth=self.cleaned_data['date_of_birth'],
            email=self.cleaned_data['email'],
            production=self.cleaned_data['production'],
            user=user,
        )

        if commit:
            profile.save()
        return user

    class Meta:
        model = Profile
        fields = (
            'username', 'password', 'password2', 'first_name', 'last_name', 'image')
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter first name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter last name'
                }
            ),
            'picture': forms.TextInput(
                attrs={
                    'placeholder': 'Enter URL'
                }
            ),
        }


class LoginProfileForm(BootstrapFormMixin, forms.ModelForm):
    pass


class EditProfileForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self.initial['production'] = Profile.VEG_FRUT

    class Meta:
        model = Profile
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
            'image': forms.TextInput(
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

