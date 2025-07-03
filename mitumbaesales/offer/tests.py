from django.test import TestCase
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError 
from datetime import date, timedelta
import uuid

from .models import Offer, Discount, OfferDiscount

class OfferModelTest(TestCase):
    def test_offer_creation(self):
        """Test the creation of an Offer instance."""
        offer = Offer.objects.create(
            name='Summer Sale',
            description='Discounts on summer items',
            offer_type='seasonal',
            start_date=date(2025, 6, 1),
            end_date=date(2025, 6, 30),
            is_active=True,
            priority=1,
            usage_limit=100,
            uses_count=0,
            applies_to='all'
        )
        self.assertIsNotNone(offer.offer_id)
        self.assertEqual(offer.name, 'Summer Sale')
        self.assertTrue(offer.is_active)
        self.assertEqual(offer.usage_limit, 100)
        self.assertEqual(offer.uses_count, 0)
        self.assertEqual(offer.applies_to, 'all')
        self.assertIsNotNone(offer.created_at)
        self.assertIsNotNone(offer.updated_at)

    def test_string_representation(self):
        """Test the string representation of the Offer model."""
        offer = Offer(name='New Year Sale')
        self.assertEqual(str(offer), 'New Year Sale')

    def test_offer_defaults(self):
        """Test default values for Offer fields."""
        offer = Offer.objects.create(
            name='Default Offer',
            offer_type='general',
            start_date=date(2025, 1, 1),
            end_date=date(2025, 12, 31)
        )
        self.assertTrue(offer.is_active)
        self.assertEqual(offer.priority, 0)
        self.assertEqual(offer.usage_limit, 0)
        self.assertEqual(offer.uses_count, 0)
       
        self.assertEqual(offer.applies_to, '')
        self.assertIsNone(offer.description) 

    def test_offer_update(self):
        """Test updating an existing Offer instance."""
        offer = Offer.objects.create(
            name='Original Offer',
            offer_type='promo',
            start_date=date(2025, 1, 1),
            end_date=date(2025, 1, 31),
            is_active=True
        )
        offer.name = 'Updated Offer Name'
        offer.is_active = False
        offer.save()

        updated_offer = Offer.objects.get(pk=offer.pk)
        self.assertEqual(updated_offer.name, 'Updated Offer Name')
        self.assertFalse(updated_offer.is_active)
        self.assertGreater(updated_offer.updated_at, offer.created_at)

    def test_offer_deletion(self):
        """Test deleting an Offer instance."""
        offer = Offer.objects.create(
            name='Offer to Delete',
            offer_type='test',
            start_date=date(2025, 1, 1),
            end_date=date(2025, 1, 1)
        )
        offer_id = offer.offer_id
        offer.delete()
        self.assertFalse(Offer.objects.filter(pk=offer_id).exists())


class DiscountModelTest(TestCase):
    def test_discount_creation(self):
        """Test the creation of a Discount instance."""
        discount = Discount.objects.create(
            discount_id='DISC123',
            name='Holiday Discount',
            discount_type='percentage',
            value=15.00,
            min_purchase_amount=50.00,
            max_purchase_amount=200.00,
            is_active=True
        )
        self.assertEqual(discount.discount_id, 'DISC123')
        self.assertEqual(discount.name, 'Holiday Discount')
        self.assertEqual(discount.discount_type, 'percentage')
        self.assertEqual(float(discount.value), 15.0)
        self.assertEqual(float(discount.min_purchase_amount), 50.0)
        self.assertEqual(float(discount.max_purchase_amount), 200.0)
        self.assertTrue(discount.is_active)

    def test_string_representation(self):
        """Test the string representation of the Discount model."""
        discount = Discount(discount_id='TESTDISC', name='Test Discount')
        self.assertEqual(str(discount), 'Test Discount (TESTDISC)')

    def test_discount_type_choices(self):
        """Test that discount_type adheres to choices by raising ValidationError."""
        valid_discount = Discount.objects.create(
            discount_id='VALID1', name='Valid', discount_type='percentage', value=10.0
        )
        self.assertEqual(valid_discount.discount_type, 'percentage')

     
        invalid_discount = Discount(
            discount_id='INVALID1',
            name='Invalid',
            discount_type='invalid_type', 
            value=10.0
        )
        

        with self.assertRaises(ValidationError) as cm:
            invalid_discount.full_clean()

       
        self.assertIn("Value 'invalid_type' is not a valid choice.", str(cm.exception))


class OfferDiscountModelTest(TestCase):
    def setUp(self):
        """Set up an Offer and a Discount for OfferDiscount tests."""
        self.offer = Offer.objects.create(
            name='Test Offer',
            offer_type='general',
            start_date=date(2025, 1, 1),
            end_date=date(2025, 1, 31)
        )
        self.discount = Discount.objects.create(
            discount_id='TESTDISC001',
            name='Test Discount',
            discount_type='fixed_amount',
            value=10.00
        )

    def test_offer_discount_creation(self):
        """Test the creation of an OfferDiscount instance."""
        offer_discount = OfferDiscount.objects.create(
            offer=self.offer,
            discount=self.discount
        )
        self.assertIsNotNone(offer_discount.offer_discount_id)
        self.assertEqual(offer_discount.offer, self.offer)
        self.assertEqual(offer_discount.discount, self.discount)

    def test_string_representation(self):
        """Test the string representation of the OfferDiscount model."""
        offer_discount = OfferDiscount.objects.create(
            offer=self.offer,
            discount=self.discount
        )
        expected_str = f"Offer '{self.offer.name}' linked to Discount '{self.discount.name}'"
        self.assertEqual(str(offer_discount), expected_str)

    def test_unique_together_constraint(self):
        """Test that an Offer and Discount can only be linked once."""
        OfferDiscount.objects.create(offer=self.offer, discount=self.discount)
        with self.assertRaises(IntegrityError):
            OfferDiscount.objects.create(offer=self.offer, discount=self.discount)

    def test_cascade_on_offer_deletion(self):
        """Test that OfferDiscount is deleted when related Offer is deleted."""
        offer_discount = OfferDiscount.objects.create(offer=self.offer, discount=self.discount)
        offer_discount_id = offer_discount.offer_discount_id
        self.offer.delete()
        self.assertFalse(OfferDiscount.objects.filter(pk=offer_discount_id).exists())
        self.assertTrue(Discount.objects.filter(pk=self.discount.pk).exists())

    def test_cascade_on_discount_deletion(self):
        """Test that OfferDiscount is deleted when related Discount is deleted."""
        offer_discount = OfferDiscount.objects.create(offer=self.offer, discount=self.discount)
        offer_discount_id = offer_discount.offer_discount_id
        self.discount.delete()
        self.assertFalse(OfferDiscount.objects.filter(pk=offer_discount_id).exists())
        self.assertTrue(Offer.objects.filter(pk=self.offer.pk).exists())
