from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from authentication.models import User  
from product.models import Product 
from orders.models import Order, OrderItem
from payments.models import Payment, DarajaAPI
from offer.models import Offer, Discount
from reviews.models import Review, RateTrader
from cart.models import Cart, CartItem
from notification.models import Notification
from .serializers import (
    PaymentsSerializers,
    OfferSerializer,
    DiscountSerializer,
    OrderSerializer,
    OrderItemSerializer,
    ProductSerializer,
    UserSerializer,
    ReviewSerializer,
    RateTraderSerializer,
    CartSerializer,
    CartItemSerializer,
    STKPushSerializer
)


# Create your views here.

class PaymentsViewset(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentsSerializers


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class RateTraderViewSet(viewsets.ModelViewSet):
    queryset = RateTrader.objects.all()
    serializer_class = RateTraderSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class STKPushView(APIView):
   def post(self, request):
       serializer = STKPushSerializer(data=request.data)
       if serializer.is_valid():
           data = serializer.validated_data
           daraja = DarajaAPI()
           response = daraja.stk_push(
               phone_number=data['phone_number'],
               amount=data['amount'],
               account_reference=data['account_reference'],
               transaction_desc=data['transaction_desc']
           )
           return Response(response)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['POST'])
def daraja_callback(request):
    print("Daraja Callback Data:", request.data)
    return Response({"ResultCode": 0, "ResultDesc": "Accepted"})




