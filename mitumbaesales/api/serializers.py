
from rest_framework import serializers
from offer.models import Offer, Discount, OfferDiscount 
from django.contrib.auth import get_user_model

User = get_user_model()

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'


