from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}), 
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role',)}),  
    )
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')  
    list_filter = ('role', 'is_staff', 'is_active')  
    search_fields = ('username', 'email') 
