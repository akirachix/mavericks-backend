from rest_framework import serializers
from reviews.models import Review
from reviews.models import RateTrader
from cart.models import Cart, CartItem




class ReviewSerializer(serializers.ModelSerializer):
   class Meta:
       model = Review
       fields = '__all__'






class RateTraderSerializer(serializers.ModelSerializer):
   class Meta:
       model = RateTrader
       fields = '__all__'






class CartItemSerializer(serializers.ModelSerializer):
   class Meta:
       model = CartItem
       fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
   items = CartItemSerializer(many=True, read_only=True)


   class Meta:
       model = Cart
       fields = '__all__'