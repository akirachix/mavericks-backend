from django.db import models

# Create your models here.

from authentication.models import User  
from product.models import Product 
from offer.models import Offer,Discount



from rest_framework import serializers

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'
class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'

        

