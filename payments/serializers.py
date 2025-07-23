from rest_framework import serializers
from .models import MpesaSTKPush

class MpesaSTKPushInitiateSerializer(serializers.Serializer):

    phone_number = serializers.CharField(max_length=12, help_text="M-Pesa registered phone number (e.g., 2547XXXXXXXX).")
    amount = serializers.DecimalField(max_digits=10, decimal_places=2, min_value=1)
    reference = serializers.CharField(max_length=100, required=False, help_text="Internal transaction reference.")
    description = serializers.CharField(max_length=255, required=False, help_text="Short description of the transaction.")

    def validate_phone_number(self, value):
        if not value.startswith('2547') or not value[3:].isdigit() or len(value) != 12:
            raise serializers.ValidationError("Phone number must be in the format 2547XXXXXXXX and 12 digits long.")
        return value

