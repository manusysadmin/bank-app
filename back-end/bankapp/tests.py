from .models import CustomUser
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate, APIClient



class ProductCreateTestCase(APITestCase):

    def setUp(self):
        data = {"username": "test-admin", "password": "testpassword"}
        self.superuser = CustomUser.objects.create_superuser(username="test-admin",
                                                             password="testpassword")
        self.superuser.save()

        self.user = CustomUser.objects.create_user(username='test-user', password='testpassword')
        self.user.save()

    def test_productcreate(self):
        client = APIClient()
        login_response = self.client.post("/api/login", {'username': 'test-admin',
                                                         'password': 'testpassword'}, format='json')
        token = login_response.data['access']
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        data = {"name": "testproduct",
                "age": ['JUNIOR'],
                "student": False,
                "income": ["NO_INCOME"]}
        response = client.post("/api/manage/products/add", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)

    def test_productcreate_unauthorized(self):
        client = APIClient()
        login_response = self.client.post("/api/login", {'username': 'test-user',
                                                         'password': 'testpassword'}, format='json')
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + login_response.data['access'])
        data = {"name": "testproduct",
                "age": ['JUNIOR'],
                "student": False,
                "income": ["NO_INCOME"]}
        response = client.post("/api/manage/products/add", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Product.objects.count(), 0)
