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
    SIZE_XS = 'XS'
    SIZE_S = 'S'
    SIZE_M = 'M'
    SIZE_L = 'L'
    SIZE_XL = 'XL'
    SIZE_XXL = 'XXL'
    SIZE_CHOICES = [
        (SIZE_XS, 'Extra Small'),
        (SIZE_S, 'Small'),
        (SIZE_M, 'Medium'),
        (SIZE_L, 'Large'),
        (SIZE_XL, 'Extra Large'),
        (SIZE_XXL, 'XXL'),
    ]
    AUDIENCE_MEN = 'Men'
    AUDIENCE_WOMEN = 'Women'
    AUDIENCE_KIDS = 'Kids'
    AUDIENCE_CHOICES = [
        (AUDIENCE_MEN, 'Men'),
        (AUDIENCE_WOMEN, 'Women'),
        (AUDIENCE_KIDS, 'Kids'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    audience = models.CharField(max_length=10, choices=AUDIENCE_CHOICES, default='Women')
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField(default=1)
    image = models.URLField(max_length=400)
    description = models.TextField()
    size = models.CharField(max_length=5, choices=SIZE_CHOICES) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name