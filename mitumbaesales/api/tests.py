from django.test import TestCase
from django.test import TestCase
from .models import Offer

from .models import Notification
from django.contrib.auth import get_user_model



class OfferModelTest(TestCase):
    def test_string_representation(self):
        """Test the string representation of the Offer model."""
        offer = Offer(name='New Year Sale')
        self.assertEqual(str(offer), offer.name)

    def test_offer_creation(self):
        """Test the creation of an Offer instance."""
        offer = Offer.objects.create(
            name='Summer Sale',
            description='Discounts on summer items',
            offer_type='seasonal',
            start_date='2025-06-01',
            end_date='2025-06-30',
            is_active=True,
            priority=1,
            usage_limit=100,
            uses_count=0,
            applies_to='all'
        )
        self.assertEqual(offer.name, 'Summer Sale')
        self.assertTrue(offer.is_active)
        self.assertEqual(offer.usage_limit, 100)


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