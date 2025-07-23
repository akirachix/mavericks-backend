from django.contrib import admin
from .models import AppUser
# from django.contrib.auth.models import User
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.




@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email', 'phone', 'user_type', 'created_at')
    search_fields = ('user__username', 'name', 'email', 'phone')
    list_filter = ('user_type',)




