from django.db import models

# Create your models here.
import uuid
from authentication.models import User
from django.utils import timezone
from product.models import Product
from django.core.validators import MinValueValidator, MaxValueValidator

STATUS_CHOICES = [
    ('pending', 'processed'),
    ('cancelled', 'delivered'),
]

class Order(models.Model):
    
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
   
    status = models.CharField(max_length=20, default='Pending', choices=STATUS_CHOICES)
    total_price = models.DecimalField(max_digits=10, decimal_places=2 , validators=[MinValueValidator(0.01),MaxValueValidator(1000000)], 
    null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class OrderItem(models.Model):
    
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01),MaxValueValidator(1000000)], 
    null=False, blank=False)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    added_at = models.DateTimeField(auto_now_add=True)
    def save(self, *args, **kwargs):
        self.subtotal = self.quantity * self.unit_price
        super().save(*args, **kwargs)


   





