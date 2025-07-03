from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from .models import Offer, Discount
from .serializers import OfferSerializer, DiscountSerializer

class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
   
    permission_classes = [IsAdminUser | IsAuthenticatedOrReadOnly]

class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
 
    permission_classes = [IsAdminUser | IsAuthenticatedOrReadOnly]
  
