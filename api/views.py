from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from product.models import Product 
from orders.models import Order, OrderItem
from rest_framework import viewsets, generics, permissions, status
from rest_framework.permissions import IsAuthenticated, AllowAny 
from offer.models import Offer, Discount
from reviews.models import Review, RateTrader
from cart.models import Cart, CartItem
from authentication.models import AppUser
from .serializers import AppUserSerializer
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings 
from rest_framework.exceptions import ValidationError 
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth.models import User as AuthUser 
from django.contrib.auth import authenticate, login, logout 
from .serializers import AppUserSerializer as AppUserRegistrationSerializer 
from rest_framework.authtoken.models import Token

import requests
from api.permissions import IsSellerOrReadOnly, IsOwnerOrAdmin
import base64
import json 
from datetime import datetime
from .serializers import (
    OfferSerializer,
    DiscountSerializer,
    OrderSerializer,
    OrderItemSerializer,
    ProductSerializer,
    ReviewSerializer,
    RateTraderSerializer,
    CartSerializer,
    CartItemSerializer,
    AppUserSerializer,
)

class AppUserViewSet(viewsets.ModelViewSet):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer
    permission_classes = [permissions.AllowAny] 


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)

            try:
                
                app_user_profile = user.appuser_profile
                user_type = app_user_profile.user_type
            except AppUser.DoesNotExist:
                user_type = 'Unknown' 

            return Response({
                'token': token.key,
                'user_id': user.id,
                'username': user.username,
                'email': user.email,
                'user_type': user_type
            }, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)

class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = AppUserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            app_user = serializer.save()
            return Response({'message': 'User registered successfully.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            request.user.auth_token.delete()
            return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class OrderItemListView(generics.ListCreateAPIView):
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated] 


    def get_queryset(self):
        order_pk = self.kwargs['order_pk']
        order = get_object_or_404(Order, pk=order_pk)
        if not self.request.user.is_staff and order.buyer != self.request.user.appuser:
            raise PermissionDenied("You do not have permission to access items for this order.")
        
        return OrderItem.objects.filter(order=order)


    def perform_create(self, serializer):
        order_pk = self.kwargs['order_pk']
        order = get_object_or_404(Order, pk=order_pk)


        if not self.request.user.is_staff and order.buyer != self.request.user.appuser:
            raise PermissionDenied("You do not have permission to add items to this order.")

        serializer.save(order=order)



class OrderItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        order_pk = self.kwargs['order_pk']
        order = get_object_or_404(Order, pk=order_pk)


        if not self.request.user.is_staff and order.buyer != self.request.user.appuser:
            raise PermissionDenied("You do not have permission to access items for this order.")
        
        return OrderItem.objects.filter(order=order)
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.kwargs['pk'])
        self.check_object_permissions(self.request, obj) 
        return obj

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            try:
                app_user = AppUser.objects.get(user=self.request.user)
                return Order.objects.filter(buyer=app_user).order_by('-created_at')
            except AppUser.DoesNotExist:
                return Order.objects.none()
        return Order.objects.none() 

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            try:
                app_user = AppUser.objects.get(user=self.request.user)
                serializer.save(buyer=app_user)
            except AppUser.DoesNotExist:
                raise ValidationError("Authenticated user has no associated AppUser profile. Cannot create order.")
        else:
            raise permissions.NotAuthenticated()

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer

    permission_classes = [IsSellerOrReadOnly, IsOwnerOrAdmin]

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            try:
                app_user = AppUser.objects.get(user=self.request.user)
                if app_user.user_type == 'Seller':
                    serializer.save(user=app_user)
                else:
                    raise permissions.PermissionDenied("Only Seller accounts can create products.")
            except AppUser.DoesNotExist:
                raise ValidationError("Authenticated user has no associated AppUser profile.")
        else:
            raise permissions.NotAuthenticated("Authentication credentials were not provided.")


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

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



