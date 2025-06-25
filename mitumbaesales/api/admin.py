from django.contrib import admin
from .models import Notification
from .models import Offer, Discount, OfferDiscount, OfferProduct
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('notification_id', 'user', 'message', 'notifications_type', 'is_read', 'created_at')
    list_filter = ('notifications_type', 'is_read', 'user')
    search_fields = ('message', 'user__username', 'notifications_type')

admin.site.register(Notification, NotificationAdmin)

admin.site.register(Offer)
admin.site.register(Discount)
admin.site.register(OfferDiscount)
admin.site.register(OfferProduct)
