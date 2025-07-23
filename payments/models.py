from django.db import models
from authentication.models import AppUser 

# Create your models here.

class MpesaSTKPush(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.SET_NULL, null=True, blank=True)
    phone_number = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reference = models.CharField(max_length=100, unique=True, null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    checkout_request_id = models.CharField(max_length=100, unique=True, null=True, blank=True)
    merchant_request_id = models.CharField(max_length=100, unique=True, null=True, blank=True)
    response_code = models.CharField(max_length=10, null=True, blank=True)
    response_description = models.TextField(blank=True, null=True)
    customer_message = models.TextField(blank=True, null=True)

    result_code = models.CharField(max_length=10, null=True, blank=True)
    result_description = models.TextField(blank=True, null=True)
    mpesa_receipt_number = models.CharField(max_length=50, null=True, blank=True)
    transaction_date = models.DateTimeField(null=True, blank=True)
    phone_number_from_callback = models.CharField(max_length=15, null=True, blank=True)
    amount_from_callback = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    status_choices = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Failed', 'Failed'),
        ('Cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='Pending')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Mpesa STK Push for {self.phone_number} - {self.amount} - {self.status}"

