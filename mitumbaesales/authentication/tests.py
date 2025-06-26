# # from django.urls import reverse
# # from rest_framework import status
# # from rest_framework.test import APITestCase
# # from authentication.models import User
# # from product.models import Product
# # from django.core.files.uploadedfile import SimpleUploadedFile 

# # class ProductAPITests(APITestCase):
# #     def setUp(self):
# #         self.user = User.objects.create(
# #             name="Seller",
# #             email="seller@example.com",
# #             phone="1112223333",
# #             password="password",
# #             user_type="Seller"
# #         )
# #         self.product_data = {
# #             "user": str(self.user.user),  
# #             "category": "High-Quality",
# #             "audience": "Women",
# #             "name": "Blue Shirt",
# #             "price": "29.99",
# #             "stock_quantity": 10,
# #             "description": "A stylish blue shirt.",
# #             "size": "M",
# #             "image": SimpleUploadedFile("test.jpg", b"file_content", content_type="image/jpeg"),
            
# #         }

# #     def test_create_product(self):
# #         url = reverse('product-list')
# #         response = self.client.post(url, self.product_data, format='multipart')
# #         print("DEBUG:", response.data)
# #         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
# #         self.assertEqual(Product.objects.count(), 1)
# #         self.assertEqual(Product.objects.get().name, self.product_data['name'])

# #     def test_list_products(self):
# #         Product.objects.create(
# #             user=self.user,
# #             category="Fashion Finds",
# #             audience="Men",
# #             name="Red Hat",
# #             price=200,
# #             stock_quantity=5,
# #             description="A trendy red hat.",
# #             size="L",
# #             # image=SimpleUploadedFile("dummy.jpg", b"dummy_content", content_type="image/jpeg")
# #         )
# #         url = reverse('product-list')
# #         response = self.client.get(url, format='json')
# #         self.assertEqual(response.status_code, status.HTTP_200_OK)
# #         self.assertEqual(len(response.data), 1)




# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase
# from authentication.models import User
# from django.core.files.uploadedfile import SimpleUploadedFile
# from io import BytesIO
# from PIL import Image

# def get_temporary_image():
#     img_io = BytesIO()
#     image = Image.new('RGB', (100, 100), color='red')
#     image.save(img_io, 'JPEG')
#     img_io.seek(0)
#     return SimpleUploadedFile('test.jpg', img_io.read(), content_type='image/jpeg')

# class ProductAPITests(APITestCase):
#     def setUp(self):
#         self.user = User.objects.create(
#             name="Seller",
#             email="seller@example.com",
#             phone="1112223333",
#             password="password",
#             user_type="Seller"
#         )
#         self.product_data = {
#             "user": str(self.user.user),
#             "category": "High-Quality",
#             "audience": "Women",
#             "name": "Blue Shirt",
#             "price": "29.99",
#             "stock_quantity": 10,
#             "description": "A stylish blue shirt.",
#             "size": "M",
#             "image": get_temporary_image(),
#         }

#     def test_create_product(self):
#         url = reverse('product-list')
#         response = self.client.post(url, self.product_data, format='multipart')
#         print("DEBUG:", response.data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)














from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from authentication.models import User

class UserAPITests(APITestCase):
    def setUp(self):
        self.user_data = {
            "name": "Test User",
            "email": "testuser@example.com",
            "phone": "1234567890",
            "password": "password123",
            "user_type": "Customer",
        }
        self.user = User.objects.create(**self.user_data)

    def test_create_user(self):
        url = reverse('user-list')  # adjust if your endpoint is different
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