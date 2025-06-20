from django.db import models
import uuid
from users.models import User
from catalogue.models import Product
# Create your models here.
class Review(models.Model):
    review_id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(
        choices=[(i, str(i)) for i in range(1, 6)],
        null=False
    )
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class TraderRating(models.Model):
    rate_trader_id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    buyer = models.ForeignKey(User, related_name='buyer_ratings', on_delete=models.CASCADE)
    seller = models.ForeignKey(User, related_name='seller_ratings', on_delete=models.CASCADE)
    rating = models.IntegerField(
        choices=[(i, str(i)) for i in range(1, 6)],
        null=False
    )
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
