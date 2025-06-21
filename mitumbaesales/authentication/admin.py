from django.contrib import admin
from .models import User 

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email', 'phone', 'user_type', 'created_at')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('user_type',)


admin.site.register(User, UserAdmin)