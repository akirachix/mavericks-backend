from rest_framework import viewsets
from django.shortcuts import render
from .models import Offer, Discount
from .serializers import (OfferSerializer, DiscountSerializer)

class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer

# class OfferDiscountViewSet(viewsets.ModelViewSet):
#     queryset = OfferDiscount.objects.all()
#     serializer_class = OfferDiscountSerializer

# class OfferProductViewSet(viewsets.ModelViewSet):
#     queryset = OfferProduct.objects.all()
#     serializer_class = OfferProductSerializer
#     from django.shortcuts import render
# from rest_framework import viewsets
from .models import Notification
from .serializers import NotificationSerializer

# Create your views here.

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer