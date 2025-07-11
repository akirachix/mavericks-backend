from django.db import models
from django.core.exceptions import ValidationError
import uuid 

# Create your models here.
class User(models.Model):
    USER_TYPE_CHOICES = [
        ('Buyer', 'Buyer'),
        ('Seller', 'Seller'),
    ]

    user = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True, null=True, blank=True)
    phone = models.CharField(max_length=15, unique=True, null=True, blank=True)
    password = models.CharField(max_length=100)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if not self.email and not self.phone:
            raise ValidationError("Either email or phone must be provided.")

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(email__isnull=False) | models.Q(phone__isnull=False),
                name='email_or_phone_check'
            ),
        ]
    def __str__(self):
        return self.name
