from django.shortcuts import render
from rest_framework import viewsets


# Create your views here.
from payments.models import Payment
from .serializers import paymentsSerializers
class paymentsViewset(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = paymentsSerializers

