from rest_framework import serializers

from payments.models import Payment

class paymentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

from .models import Product, User
from product.models import Product
from authentication.models import User

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



