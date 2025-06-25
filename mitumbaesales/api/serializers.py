from rest_framework import serializers
from payment.models import Payment, PaymentTransfer

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class PaymentTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentTransfer
        fields = '__all__'