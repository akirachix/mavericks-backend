from django.contrib import admin



from .models import Order
admin.site.register(Order)

from .models import OrderItem
admin.site.register(OrderItem)
# admin.site.register(Product)

