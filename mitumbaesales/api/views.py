
from django.shortcuts import render
from rest_framework import viewsets


# Create your views here.
from payments.models import Payment
from .serializers import paymentsSerializers
class paymentsViewset(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = paymentsSerializers


from rest_framework import viewsets
from .models import Product, User
from product.models import Product
from authentication.models import User
from .serializers import ProductSerializer, UserSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer




