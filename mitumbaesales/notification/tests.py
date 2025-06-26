from django.test import TestCase
from .models import Notification
from django.contrib.auth import get_user_model

User = get_user_model()

class NotificationModelTest(TestCase):
    def setUp(self):
        """Create a user for testing."""
        self.user = User.objects.create(username='testuser')

    def test_string_representation(self):
        """Test the string representation of the Notification model."""
        notification = Notification.objects.create(
            user=self.user,
            message='Your order has been shipped.',
            notifications_type='Order update'
        )
        self.assertEqual(str(notification), f"Order update for {self.user.username}")

    def test_notification_creation(self):
        """Test the creation of a Notification instance."""
        notification = Notification.objects.create(
            user=self.user,
            message='Your payment has been confirmed.',
            notifications_type='Payment Confirmation'
        )
        self.assertEqual(notification.message, 'Your payment has been confirmed.')
        self.assertFalse(notification.is_read)