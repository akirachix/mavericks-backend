from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from authentication.models import User

class UserAPITests(APITestCase):
    def setUp(self):
        self.user_data = {
            "name": "Test User",
            "email": "testuser@example.com",
            "phone": "+251704567890",
            "password": "password123",
            "user_type": "Buyer",
        }
        self.user = User.objects.create(**self.user_data)

    def test_create_user(self):
        url = reverse('user-list') 
        data = {
            "name": "New User",
            "email": "newuser@example.com",
            "phone": "0987654321",
            "password": "password456",
            "user_type": "Seller",
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_user(self):
        url = reverse('user-detail', args=[self.user.pk])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], self.user.email)

    def test_update_user(self):
        url = reverse('user-detail', args=[self.user.pk])
        update_data = {"name": "Updated Name"}
        response = self.client.patch(url, update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Updated Name")

    def test_delete_user(self):
        url = reverse('user-detail', args=[self.user.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(User.objects.filter(pk=self.user.pk).exists())