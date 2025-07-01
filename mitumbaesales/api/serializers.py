from rest_framework import serializers
from .models import Offer, Discount

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'



class OfferSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Offer
        fields = '__all__'

from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
