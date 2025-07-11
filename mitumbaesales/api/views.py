from rest_framework import viewsets, serializers
from payments.models import Payment, PaymentTransfer

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class PaymentTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentTransfer
        fields = '__all__'

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class PaymentTransferViewSet(viewsets.ModelViewSet):
    queryset = PaymentTransfer.objects.all()
    serializer_class = PaymentTransferSerializer