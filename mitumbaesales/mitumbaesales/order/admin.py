from django.contrib import admin
from .models import order
from .models import OrderItem

# Register your models here.

admin.site.Register(Order)
admin.site.Register(Order_status)