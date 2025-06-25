from rest_framework import viewsets
from .models import Offer, Discount, OfferDiscount, OfferProduct, Notification
from .serializers import (
    OfferSerializer,
    DiscountSerializer,
    OfferDiscountSerializer,
    OfferProductSerializer,
    NotificationSerializer,
)

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

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer