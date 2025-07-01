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

from .models import Notification
from .serializers import NotificationSerializer



class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer