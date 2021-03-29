from bankapp.models import CustomUser, Product
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate, APIClient, APIRequestFactory


class UserTestCases(APITestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(username="test-user", password="testpassword")
        self.user.save()
        self.assertEqual(CustomUser.objects.count(), 1)

        self.superuser = CustomUser.objects.create_superuser(username="test-admin", password="testpassword")
        self.superuser.save()
        self.assertEqual(CustomUser.objects.count(), 2)

    def test_user_create(self):
        response = self.client.post("/api/register", {"username": "test-user-reg", "password": "testpassword"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 3)

    def test_user_login(self):
        response = self.client.post("/api/login", {"username": "test-user", "password": "testpassword"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in response.data)
        self.assertTrue('refresh' in response.data)
        client = APIClient()
        client.logout()

    def test_user_get(self):
        login_response = self.client.post("/api/login", {"username": "test-admin", "password": "testpassword"})
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + login_response.data['access'])
        response = client.get("/api/manage/users/1")
        print(response)

    def test_user_delete(self):
        login_response = self.client.post("/api/login", {"username": "test-admin", "password": "testpassword"})
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + login_response.data['access'])
        response = client.delete("/api/manage/users/1")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(CustomUser.objects.count(), 2)


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
