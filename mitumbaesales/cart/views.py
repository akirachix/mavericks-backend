<<<<<<< HEAD
from django.shortcuts import render
=======
>>>>>>> 43336c22a839c4a7d795b6237da2a3de789c8f3b
from rest_framework import viewsets
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer

<<<<<<< HEAD
# Create your views here.
=======
>>>>>>> 43336c22a839c4a7d795b6237da2a3de789c8f3b
class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
<<<<<<< HEAD
    serializer_class = CartItemSerializer
=======
    serializer_class = CartItemSerializer
>>>>>>> 43336c22a839c4a7d795b6237da2a3de789c8f3b
