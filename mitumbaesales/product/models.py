from django.db import models
from authentication.models import User
import uuid
# Create your models here.
class Product(models.Model):
    HIGH_QUALITY = 'High-Quality'
    FASHION_FINDS = 'Fashion Finds'
    CATEGORY_CHOICES = [
        (HIGH_QUALITY, 'High-Quality'),
        (FASHION_FINDS, 'Fashion Finds'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField(default=1)
    image = models.ImageField(upload_to='product_images/')
    description = models.TextField()
    size = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name