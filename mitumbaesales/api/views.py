from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from payment.models import Payment
from .serializers import PaymentSerializer, PaymentTransferSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class PaymentTransferViewSet(viewsets.ModelViewSet):
    queryset = PaymentTransfer.objects.all()
    serializer_class = PaymentTransferSerializer
