from django.db import models
from django.db import models
from django.conf import settings
# from authentication.models import User
import uuid

# Create your models here.
class Notification(models.Model):
    notification_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    NOTIFICATION_TYPES = [
        ('Order update', 'Order update'),
        ('Payment Confirmation', 'Payment Confirmation'),
        ('General Alert', 'General Alert'),
    ]
    notifications_type = models.CharField(max_length=20, choices=NOTIFICATION_TYPES)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.notifications_type} for {self.user}"