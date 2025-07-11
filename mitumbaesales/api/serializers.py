from rest_framework import serializers
<<<<<<< HEAD
from payments.models import Payment, PaymentTransfer

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class PaymentTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentTransfer
=======
from payments.models import Payment

class paymentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Payment
>>>>>>> feature/boilerplate
        fields = '__all__'