from django.shortcuts import render
from rest_framework import viewsets
from authentication.models import User  
from product.models import Product 
from orders.models import Order, OrderItem
from payments.models import Payment
from offer.models import Offer, Discount
from reviews.models import Review, RateTrader
from cart.models import Cart, CartItem
from notifications.models import Notification
from .serializers import (
    PaymentsSerializers,
    OfferSerializer,
    DiscountSerializer,
    OrderSerializer,
    OrderItemSerializer,
    ProductSerializer,
    UserSerializer,
    ReviewSerializer,
    RateTraderSerializer,
    CartSerializer,
    CartItemSerializer
   
)

# Create your views here.

class PaymentsViewset(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = paymentsSerializers


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class RateTraderViewSet(viewsets.ModelViewSet):
    queryset = RateTrader.objects.all()
    serializer_class = RateTraderSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer



