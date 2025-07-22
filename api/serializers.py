from rest_framework import serializers
from product.models import Product
from orders.models import Order, OrderItem
from offer.models import Offer, Discount
from reviews.models import Review, RateTrader
from cart.models import Cart, CartItem
from django.contrib.auth.models import User as AuthUser
from authentication.models import AppUser
from django.contrib.auth.models import User as AuthUser
from .models import AppUser



class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_price = serializers.DecimalField(source='product.price', max_digits=10, decimal_places=2, read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), source='product', write_only=True
    )

    class Meta:
        model = OrderItem
        fields = ['id', 'product_id', 'product_name', 'product_price', 'quantity', 'unit_price', 'subtotal', 'added_at']
        read_only_fields = ['subtotal', 'added_at', 'product_name', 'product_price']


class OrderSerializer(serializers.ModelSerializer):
    buyer = serializers.PrimaryKeyRelatedField(read_only=True)
    order_items = OrderItemSerializer(many=True, write_only=True, required=False)
    display_order_items = OrderItemSerializer(source='order_items', many=True, read_only=True)
    class Meta:
        model = Order
        fields = [
            'id', 'buyer', 'status', 'total_price', 'created_at', 'updated_at',
            'order_items',         
            'display_order_items'   
        ]
        read_only_fields = ['total_price', 'created_at', 'updated_at']



    def create(self, validated_data):
        order_items_data = validated_data.pop('order_items', [])
        initial_total_price = validated_data.pop('total_price', None) 
        order = super().create(validated_data)

        total_price_calculated = 0
        for item_data in order_items_data:
            try:
                product = Product.objects.get(id=item_data['product'].id if isinstance(item_data['product'], Product) else item_data['product'])
            except Product.DoesNotExist:
                raise serializers.ValidationError(
                    f"Product with ID {item_data['product']} not found for OrderItem."
                )

            order_item = OrderItem.objects.create(order=order, product=product,
                                                  quantity=item_data['quantity'],
                                                  unit_price=item_data['unit_price'])
            total_price_calculated += order_item.subtotal

        order.total_price = total_price_calculated
        order.save()

        return order


class AuthUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = AuthUser 
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = AuthUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user
    def validate_email(self, value):
        if AuthUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value


class AppUserSerializer(serializers.ModelSerializer):
    user = AuthUserSerializer()

    class Meta:
        model = AppUser
        fields = ['user', 'name', 'email', 'phone', 'user_type']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        auth_user_serializer = self.fields['user']
        auth_user_instance = auth_user_serializer.create(user_data)
        app_user = AppUser.objects.create(user=auth_user_instance, **validated_data)
        return app_user




class ProductSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
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
