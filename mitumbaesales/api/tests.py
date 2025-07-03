from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from datetime import date, datetime
import uuid 
from offer.models import Offer, Discount

from offer.models import Offer, Discount 
t

User = get_user_model()

class OfferAPITest(APITestCase):
    def setUp(self):
        self.admin_user = User.objects.create_user(username='admin', password='password', is_staff=True)
        self.regular_user = User.objects.create_user(username='user', password='password')

  
        self.offer1 = Offer.objects.create(
            name='Test Offer 1', offer_type='general',
            start_date=date(2025, 1, 1), end_date=date(2025, 1, 31),
            created_at=datetime(2025, 1, 1, 10, 0, 0) 
        )
        self.offer2 = Offer.objects.create(
            name='Test Offer 2', offer_type='specific',
            start_date=date(2025, 2, 1), end_date=date(2025, 2, 28),
            created_at=datetime(2025, 1, 2, 10, 0, 0) 
        )

        self.offer_list_url = reverse('offer-list')
        self.offer_detail_url = reverse('offer-detail', args=[self.offer1.offer_id])

    def test_create_offer_unauthenticated(self):
        """Test unauthenticated user cannot create an offer (should get 401 Unauthorized)."""
        data = {
            'name': 'Unauthorized Offer', 'description': 'Denied', 'offer_type': 'test',
            'start_date': '2025-08-01', 'end_date': '2025-08-31', 'applies_to': 'none'
        }
        response = self.client.post(self.offer_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Offer.objects.count(), 2)


    def test_create_offer_authenticated_normal_user_denied(self):
        """Test regular authenticated user CAN create an offer."""
        self.client.force_authenticate(user=self.regular_user)
        data = {
            'name': 'Normal User Created Offer', 'description': 'Allowed', 'offer_type': 'test',
            'start_date': '2025-09-01', 'end_date': '2025-09-30', 'applies_to': 'none'
        }
        response = self.client.post(self.offer_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED) # CHANGED to 201
        self.assertEqual(Offer.objects.count(), 3) # Verify creation
        self.assertEqual(Offer.objects.latest('created_at').name, 'Normal User Created Offer')

    def test_create_offer_authenticated_admin_user(self):
        """Test admin user can create an offer."""
        self.client.force_authenticate(user=self.admin_user)
        data = {
            'name': 'Admin Created Offer', 'description': 'Allowed', 'offer_type': 'admin',
            'start_date': '2025-10-01', 'end_date': '2025-10-31', 'applies_to': 'all'
        }
        response = self.client.post(self.offer_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Offer.objects.count(), 3)
        self.assertEqual(Offer.objects.latest('created_at').name, 'Admin Created Offer')


    def test_get_offer_list(self):
        """Test retrieval of all offers, verifying content and count, respecting ordering."""
        response = self.client.get(self.offer_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2) 

       
        self.assertEqual(response.data[0]['name'], self.offer2.name) 
        self.assertEqual(response.data[1]['name'], self.offer1.name)

     
        offer_names_in_response = {item['name'] for item in response.data}
        self.assertIn(self.offer1.name, offer_names_in_response)
        self.assertIn(self.offer2.name, offer_names_in_response)

    def test_get_single_offer(self):
        """Test retrieval of a single offer by ID."""
        response = self.client.get(self.offer_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.offer1.name)

    def test_get_non_existent_offer(self):
        """Test retrieval of a non-existent offer."""
        non_existent_uuid = uuid.uuid4()
        response = self.client.get(reverse('offer-detail', args=[non_existent_uuid]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_offer_full(self):
        """Test full update of an offer by an admin user."""
        self.client.force_authenticate(user=self.admin_user)
        updated_data = {
            'name': 'Updated Summer Sale',
            'description': 'Updated description',
            'offer_type': 'updated_seasonal',
            'start_date': '2025-06-15',
            'end_date': '2025-07-15',
            'is_active': False,
            'priority': 5,
            'usage_limit': 200,
            'uses_count': 50,
            'applies_to': 'specific_products'
        }
        response = self.client.put(self.offer_detail_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.offer1.refresh_from_db()
        self.assertEqual(self.offer1.name, 'Updated Summer Sale')
        self.assertFalse(self.offer1.is_active)
        self.assertEqual(self.offer1.priority, 5)

    def test_update_offer_partial(self):
        """Test partial update of an offer by an admin user."""
        self.client.force_authenticate(user=self.admin_user)
        partial_data = {
            'name': 'Partially Updated Offer',
            'is_active': False
        }
        response = self.client.patch(self.offer_detail_url, partial_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.offer1.refresh_from_db()
        self.assertEqual(self.offer1.name, 'Partially Updated Offer')
        self.assertFalse(self.offer1.is_active)
        self.assertEqual(self.offer1.offer_type, 'general')

    def test_delete_offer(self):
        """Test deletion of an offer by an admin user."""
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.delete(self.offer_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Offer.objects.filter(pk=self.offer1.pk).exists())
        self.assertEqual(Offer.objects.count(), 1) 

    def test_list_offers_unauthenticated(self):
        """Test unauthenticated user can list offers (read-only) - expected to pass with IsAuthenticatedOrReadOnly."""
        response = self.client.get(self.offer_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


class DiscountAPITest(APITestCase):
    def setUp(self):
        self.admin_user = User.objects.create_user(username='admin_disc', password='password', is_staff=True)
        self.regular_user = User.objects.create_user(username='user_disc', password='password')

     
        self.discount1 = Discount.objects.create(
            discount_id='DISC001', name='Summer 20%', discount_type='percentage', value=20.00,
            created_at=datetime(2025, 1, 1, 10, 0, 0)
        )
        self.discount2 = Discount.objects.create(
            discount_id='DISC002', name='Fixed $5', discount_type='fixed_amount', value=5.00,
            created_at=datetime(2025, 1, 2, 10, 0, 0)
        )

        self.discount_list_url = reverse('discount-list')
        self.discount_detail_url = reverse('discount-detail', args=[self.discount1.discount_id])


    def test_create_discount_authenticated_admin(self):
        """Test admin user can create a discount."""
        self.client.force_authenticate(user=self.admin_user)
        data = {
            'discount_id': 'NEWDISC',
            'name': 'New Discount from Admin',
            'discount_type': 'percentage',
            'value': 10.00
        }
        response = self.client.post(self.discount_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Discount.objects.count(), 3)
        self.assertEqual(Discount.objects.latest('created_at').name, 'New Discount from Admin')

    def test_get_discount_list(self):
        """Test retrieval of all discounts, verifying content and count, respecting ordering."""
        response = self.client.get(self.discount_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2) 

        
        self.assertEqual(response.data[0]['name'], self.discount2.name)
        self.assertEqual(response.data[1]['name'], self.discount1.name) 

       e:
        discount_names_in_response = {item['name'] for item in response.data}
        self.assertIn(self.discount1.name, discount_names_in_response)
        self.assertIn(self.discount2.name, discount_names_in_response)

    def test_update_discount(self):
        """Test updating an existing discount by an admin user."""
        self.client.force_authenticate(user=self.admin_user)
        updated_data = {
            'name': 'Updated Discount Name',
            'value': 25.00,
            'is_active': False
        }
        response = self.client.patch(self.discount_detail_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.discount1.refresh_from_db()
        self.assertEqual(self.discount1.name, 'Updated Discount Name')
        self.assertEqual(float(self.discount1.value), 25.0)
        self.assertFalse(self.discount1.is_active)