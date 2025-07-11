from django.shortcuts import render


# Create your views here.
from rest_framework import viewsets
from reviews.models import Review, RateTrader
from cart.models import Cart, CartItem
from .serializers import ReviewSerializer, RateTraderSerializer
from .serializers import CartSerializer, CartItemSerializer


# Create your views here.
class ReviewViewSet(viewsets.ModelViewSet):
   # """
   # A viewset for viewing and editing review instances.
   # """
   queryset = Review.objects.all()
   serializer_class = ReviewSerializer


class RateTraderViewSet(viewsets.ModelViewSet):
   # """
   # A viewset for viewing and editing rate trader instances.
   # """
   queryset = RateTrader.objects.all()
   serializer_class = RateTraderSerializer




# Create your views here.
class CartViewSet(viewsets.ModelViewSet):
   queryset = Cart.objects.all()
   serializer_class = CartSerializer


class CartItemViewSet(viewsets.ModelViewSet):
   queryset = CartItem.objects.all()
   serializer_class = CartItemSerializer