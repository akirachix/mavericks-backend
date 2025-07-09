from rest_framework import viewsets
from .models import Payment, PaymentTransfer
from .serializers import PaymentSerializer, PaymentTransferSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class PaymentTransferViewSet(viewsets.ModelViewSet):
    queryset = PaymentTransfer.objects.all()
    serializer_class = PaymentTransferSerializer