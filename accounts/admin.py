from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form= UserCreationForm
    form= UserChangeForm
    model =CustomUser
    list_display=['username','gender','age']
    fieldsets =UserAdmin.fieldsets + (
        (None, {"fields": ('age','gender')}),
    )
    
    add_fieldsets =UserAdmin.add_fieldsets + (
    (None, {"fields": ('age','gender')}),
    )
    
admin.site.register(CustomUser, CustomUserAdmin)

