from django.shortcuts import render
<<<<<<< HEAD

# Create your views here.
from rest_framework import viewsets
from payments.models import Payment, PaymentTransfer
from .serializers import PaymentSerializer, PaymentTransferSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class PaymentTransferViewSet(viewsets.ModelViewSet):
    queryset = PaymentTransfer.objects.all()
    serializer_class = PaymentTransferSerializer
=======
from rest_framework import viewsets


# Create your views here.
from payments.models import Payment
from .serializers import paymentsSerializers
class paymentsViewset(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = paymentsSerializers

>>>>>>> feature/boilerplate
