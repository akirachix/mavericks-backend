from django.shortcuts import render
from rest_framework import viewsets
from payments.models import Payment
from .serializers import paymentsSerializers
from .models import Product, User
from product.models import Product
from authentication.models import User
from .serializers import ProductSerializer, UserSerializer
from orders.models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer
from .models import Offer, Discount
from .serializers import OfferSerializer, DiscountSerializer

# Create your views here.

class paymentsViewset(viewsets.ModelViewSet):
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



