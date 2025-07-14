from django.db import models
import uuid
from authentication.models import User
from orders.models import Order
import requests
from django.conf import settings
from requests.auth import HTTPBasicAuth
import base64
import datetime

class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('M-Pesa', 'M-Pesa'),
    ]
    PAYMENT_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Failed', 'Failed'),
    ]
    payment_id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=30, choices=PAYMENT_METHOD_CHOICES, default='M-Pesa')
    payment_status = models.CharField(max_length=30, choices=PAYMENT_STATUS_CHOICES, default='Pending')
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    mpesa_receipt_number = models.CharField(max_length=100, blank=True, null=True)
    paid_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Payment {self.payment_id} - {self.payment_status}"


class PaymentTransfer(models.Model):
    TRANSFER_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Failed', 'Failed'),
    ]
    transfer_id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    buyer = models.ForeignKey(User, related_name='buyer_transfers', on_delete=models.CASCADE, default=1)
    seller = models.ForeignKey(User, related_name='seller_transfers', on_delete=models.CASCADE, default=1)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, default=1)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, default=1)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    platform_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    transfer_method = models.CharField(max_length=30, default='M-Pesa')
    transfer_status = models.CharField(max_length=30, choices=TRANSFER_STATUS_CHOICES, default='Pending')
    transferred_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"Transfer {self.transfer_id} - {self.transfer_status}"




class DarajaAPI:
   def __init__(self):
       self.consumer_key = settings.DARAJA_CONSUMER_KEY
       self.consumer_secret = settings.DARAJA_CONSUMER_SECRET
       self.business_shortcode = settings.DARAJA_SHORTCODE
       self.passkey = settings.DARAJA_PASSKEY
       self.base_url = "https://sandbox.safaricom.co.ke"
       self.callback_url = settings.DARAJA_CALLBACK_URL
   def get_access_token(self):
       url = f"{self.base_url}/oauth/v1/generate?grant_type=client_credentials"
       response = requests.get(url, auth=HTTPBasicAuth(self.consumer_key, self.consumer_secret))
       return response.json()['access_token']
   def stk_push(self, phone_number, amount, account_reference, transaction_desc):
       access_token = self.get_access_token()
       timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
       password = base64.b64encode(f"{self.business_shortcode}{self.passkey}{timestamp}".encode()).decode()
       headers = {
           "Authorization": f"Bearer {access_token}",
           "Content-Type": "application/json"
       }
       payload = {
           "BusinessShortCode": self.business_shortcode,
           "Password": password,
           "Timestamp": timestamp,
           "TransactionType": "CustomerPayBillOnline",
           "Amount": int(amount),
           "PartyA": phone_number,
           "PartyB": self.business_shortcode,
           "PhoneNumber": phone_number,
           "CallBackURL": self.callback_url,
           "AccountReference": account_reference, 
           "TransactionDesc": transaction_desc,
       }
       url = f"{self.base_url}/mpesa/stkpush/v1/processrequest"
       response = requests.post(url, headers=headers, json=payload)
       return response.json()