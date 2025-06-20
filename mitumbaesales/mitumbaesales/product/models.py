from django.db import models
import uuid
from authentication.models import User

PRODUCT_CATEGORY_CHOICES = [
    ('High-Quality', 'High-Quality'),
    ('Fashion Finds', 'Fashion Finds'),
]
PRODUCT_SIZE_CHOICES =[
    ('S','S'),
    ('M','M'),
    ('XS','XS'),
    ('L','L'),
    ('XL','XL'),    
]

class Product(models.Model):
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    category = models.CharField(max_length=20, choices=PRODUCT_CATEGORY_CHOICES)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField(default=1)
    image = models.JSONField() 
    description = models.TextField()
    size = models.CharField(max_length=5, choices=PRODUCT_SIZE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

