from django.contrib import admin

# Register your models here.
from .models import Payment, PaymentTransfer
admin.site.register(Payment)
admin.site.register(PaymentTransfer)

