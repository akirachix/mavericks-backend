from django.db import models
from django.db import models
import uuid
from authentication.models import User
from django.utils import timezone
from product.models import Product
# Create your models here.
STATUS_CHOICES = [
    ('pending', 'processed'),
    ('cancelled', 'delivered'),
]
user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
class Order(models.Model):
    order_id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='Pending', choices=STATUS_CHOICES)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class OrderItem(models.Model):
    order_item_id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.UUIDField()
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    added_at = models.DateTimeField(auto_now_add=True)
    def save(self, *args, **kwargs):
        self.subtotal = self.quantity * self.unit_price
        super().save(*args, **kwargs)