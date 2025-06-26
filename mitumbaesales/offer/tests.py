from django.test import TestCase
from .models import Offer

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