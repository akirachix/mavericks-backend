from rest_framework import serializers
from .models import Offer, Discount, OfferDiscount, OfferProduct, Notification

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'

class OfferDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfferDiscount
        fields = '__all__'

class OfferProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfferProduct
        fields = '__all__'

class OfferSerializer(serializers.ModelSerializer):
    offer_discounts = OfferDiscountSerializer(many=True, read_only=True)
    offer_products = OfferProductSerializer(many=True, read_only=True)
    class Meta:
        model = Offer
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'