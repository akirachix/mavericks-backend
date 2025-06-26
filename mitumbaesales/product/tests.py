from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from authentication.models import User
from product.models import Product
from django.core.files.uploadedfile import SimpleUploadedFile
from io import BytesIO
from PIL import Image

def get_temporary_image():
    img_io = BytesIO()
    image = Image.new('RGB', (100, 100), color='blue')
    image.save(img_io, 'JPEG')
    img_io.seek(0)
    return SimpleUploadedFile('test.jpg', img_io.read(), content_type='image/jpeg')

class ProductAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            name="Seller",
            email="seller@example.com",
            phone="1112223333",
            password="password",
            user_type="Seller"
        )
        self.product_data = {
            "user": str(self.user.user), 
            "category": "High-Quality",
            "audience": "Women",
            "name": "Blue Shirt",
            "price": "29.99",
            "stock_quantity": 10,
            "description": "A stylish blue shirt.",
            "size": "M",
            "image": get_temporary_image(),
        }

    def test_create_product(self):
        url = reverse('product-list')
        response = self.client.post(url, self.product_data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().name, self.product_data['name'])

    def test_retrieve_product(self):
        product = Product.objects.create(
            user=self.user,
            category="High-Quality",
            audience="Women",
            name="Blue Shirt",
            price="29.99",
            stock_quantity=10,
            description="A stylish blue shirt.",
            size="M",
            image=get_temporary_image()
        )
        url = reverse('product-detail', args=[product.pk])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], product.name)

    def test_update_product(self):
        product = Product.objects.create(
            user=self.user,
            category="High-Quality",
            audience="Women",
            name="Blue Shirt",
            price="29.99",
            stock_quantity=10,
            description="A stylish blue shirt.",
            size="M",
            image=get_temporary_image()
        )
        url = reverse('product-detail', args=[product.pk])
        update_data = {"name": "Updated Shirt"}
        response = self.client.patch(url, update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Updated Shirt")

    def test_delete_product(self):
        product = Product.objects.create(
            user=self.user,
            category="High-Quality",
            audience="Women",
            name="Blue Shirt",
            price="29.99",
            stock_quantity=10,
            description="A stylish blue shirt.",
            size="M",
            image=get_temporary_image()
        )
        url = reverse('product-detail', args=[product.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Product.objects.filter(pk=product.pk).exists())