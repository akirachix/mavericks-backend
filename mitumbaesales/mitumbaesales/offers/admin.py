from django.contrib import admin
from django.contrib import admin
from .models import Offer, Discount, OfferDiscount, OfferProduct, Product 
# Register your models here.

admin.site.register(Offer)
admin.site.register(Discount)
admin.site.register(OfferDiscount)
admin.site.register(OfferProduct)

admin.site.register(Product)