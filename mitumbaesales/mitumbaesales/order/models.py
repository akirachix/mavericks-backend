from django.db import models
import uuid

from .models import order
from .models import OrderItem
from .models import Product
from .models import User

# Create your models here.
ORDER_STATUS_CHOICES = [
    ('', 'pending'),
    ('delivered', 'processed','cancelled'),
]

class Order(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    Order_status = models.CharField(max_length=20, default='Pending',choices = ORDER_STATUS_CHOICES)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE) 
    product= models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    added_at = models.DateTimeField(auto_now_add=True)
    def save(self, *args, **kwargs):
        self.subtotal = self.quantity * self.unit_price
        super().save(*args, **kwargs)