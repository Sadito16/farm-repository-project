from django.contrib import admin
from django.contrib.auth import get_user_model

from farm_app.accounts.models import  FarmerUser

UserModel = 'accounts.FarmerUser'
@admin.register(FarmerUser)
class FarmerUserAdmin(admin.ModelAdmin):
    pass