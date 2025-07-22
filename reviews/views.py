from django.shortcuts import render
from rest_framework import viewsets
from .models import Review, RateTrader
from .serializers import ReviewSerializer, RateTraderSerializer

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
