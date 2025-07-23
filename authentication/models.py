from django.db import models
from django.core.exceptions import ValidationError
import uuid
from django.contrib.auth.models import User as AuthUser

class AppUser(models.Model): 
   USER_TYPE_CHOICES = [
       ('Buyer', 'Buyer'),
       ('Seller', 'Seller'),
   ]

   
   user = models.OneToOneField(AuthUser, on_delete=models.CASCADE, primary_key=True, related_name='appuser_profile') 
   name = models.CharField(max_length=100)
   email = models.EmailField(max_length=100, unique=True, null=True, blank=True) 
   phone = models.CharField(max_length=15, unique=True, null=True, blank=True) 
   user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)


   def clean(self):
       if not self.email and not self.phone:
           raise ValidationError("Either email or phone must be provided for AppUser.")
       if self.phone and AppUser.objects.filter(phone=self.phone).exclude(pk=self.pk).exists():
           raise ValidationError({"phone": "This phone number is already registered."})


   class Meta:
       constraints = [
           models.CheckConstraint(
               check=models.Q(email__isnull=False) | models.Q(phone__isnull=False),
               name='appuser_email_or_phone_check'
           ),
       ]

   def __str__(self):
       return self.name or self.user.username

