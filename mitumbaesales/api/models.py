from django.db import models
from rest_framework import serializers
from authentication.models import User  
from product.models import Product 
from orders.models import Order, OrderItem
from payments.models import Payment
from offer.models import Offer, Discount
from reviews.models import Review, RateTrader
from cart.models import Cart, CartItem

# Create your models here.


        

