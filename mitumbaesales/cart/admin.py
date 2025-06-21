from django.contrib import admin

# Register your models here.
from .models import Cart, CartItem

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'buyer', 'created_at', 'updated_at')
    search_fields = ('cart_id', 'buyer__username')

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart_item_id', 'cart', 'product', 'quantity', 'unit_price', 'subtotal', 'added_at')
    search_fields = ('cart_item_id', 'cart__cart_id', 'product__name')
    list_filter = ('added_at',)
