from rest_framework import serializers
from authentication.models import User  
from product.models import Product 
from orders.models import Order, OrderItem
from payments.models import Payment, DarajaAPI
from offer.models import Offer, Discount
from reviews.models import Review, RateTrader
from cart.models import Cart, CartItem




class PaymentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class RateTraderSerializer(serializers.ModelSerializer):
    class Meta:
        model = RateTrader
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'

class STKPushSerializer(serializers.Serializer):
   phone_number = serializers.CharField()
   amount = serializers.DecimalField(max_digits=10, decimal_places=2)
   account_reference = serializers.CharField()
   transaction_desc = serializers.CharField()



