from rest_framework import serializers
from payments.models import Payment

class paymentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'