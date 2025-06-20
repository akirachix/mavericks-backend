from django.contrib import admin
from .modules import Payment
from .modules import PaymentTransfer


# Register your models here.

admin.site.register(Payment)
admin.site.register(PaymentTransfer)

