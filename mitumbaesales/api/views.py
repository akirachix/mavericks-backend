from rest_framework import viewsets

from .models import Offer, Discount
from .serializers import OfferSerializer, DiscountSerializer
class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer

    

