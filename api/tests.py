from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Offer, Discount
import datetime
import uuid

# Create your tests here.

class OfferAPITest(APITestCase):
    def setUp(self):
        self.offer_data = {
            'name': 'Summer Sale',
            'description': 'Huge discounts on summer items!',
            'offer_type': 'seasonal',
            'start_date': datetime.date(2025, 7, 1),
            'end_date': datetime.date(2025, 7, 31),
            'is_active': True,
            'priority': 10,
            'usage_limit': 1000,
            'uses_count': 0,
            'applies_to': 'all_products'
        }
        self.offer = Offer.objects.create(**self.offer_data)
        self.list_url = reverse('offer-list')
        self.detail_url = reverse('offer-detail', kwargs={'pk': self.offer.offer_id})
    def test_create_offer(self):
        new_offer_data = {
            'name': 'Winter Clearance',
            'description': 'End of season discounts!',
            'offer_type': 'clearance',
            'start_date': datetime.date(2025, 12, 1),
            'end_date': datetime.date(2025, 12, 31),
            'is_active': True,
            'priority': 5,
            'usage_limit': 500,
            'uses_count': 0,
            'applies_to': 'winter_collection'
        }
        response = self.client.post(self.list_url, new_offer_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Offer.objects.count(), 2)
        self.assertEqual(Offer.objects.get(name='Winter Clearance').description, 'End of season discounts!')
    def test_retrieve_offer(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.offer_data['name'])
    def test_update_offer(self):
        updated_data = {'name': 'Summer Sale Updated', 'priority': 20}
        response = self.client.patch(self.detail_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.offer.refresh_from_db()
        self.assertEqual(self.offer.name, 'Summer Sale Updated')
        self.assertEqual(self.offer.priority, 20)
    def test_delete_offer(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Offer.objects.count(), 0)
class DiscountAPITest(APITestCase):
    def setUp(self):
        self.discount_data = {
            'discount_id': 'DISC001',
            'name': '10% Off',
            'discount_type': 'percentage',
            'value': '10.00',
            'min_purchase_amount': '50.00',
        }
        self.discount = Discount.objects.create(**self.discount_data)
        self.list_url = reverse('discount-list')
        self.detail_url = reverse('discount-detail', kwargs={'pk': self.discount.discount_id})
    def test_create_discount(self):
        new_discount_data = {
            'discount_id': 'FIXED20',
            'name': 'Fixed $20 Off',
            'discount_type': 'fixed_amount',
            'value': '20.00',
            'min_purchase_amount': '100.00',
        }
        response = self.client.post(self.list_url, new_discount_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Discount.objects.count(), 2)
        self.assertEqual(Discount.objects.get(discount_id='FIXED20').name, 'Fixed $20 Off')
    def test_retrieve_discount(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.discount_data['name'])
    def test_update_discount(self):
        updated_data = {'name': '15% Off', 'value': '15.00'}
        response = self.client.patch(self.detail_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.discount.refresh_from_db()
        self.assertEqual(self.discount.name, '15% Off')
        self.assertEqual(str(self.discount.value), '15.00')
    def test_delete_discount(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Discount.objects.count(), 0)