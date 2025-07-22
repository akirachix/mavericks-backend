from django.shortcuts import render
from rest_framework import viewsets
from .models import Offer, Discount, OfferDiscount, OfferProduct
from .serializers import (
    OfferSerializer,
    DiscountSerializer,
    OfferDiscountSerializer,
    OfferProductSerializer,
)

# Create your views here.

class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer

class OfferDiscountViewSet(viewsets.ModelViewSet):
    queryset = OfferDiscount.objects.all()
    serializer_class = OfferDiscountSerializer

class OfferProductViewSet(viewsets.ModelViewSet):
    queryset = OfferProduct.objects.all()
    serializer_class = OfferProductSerializer