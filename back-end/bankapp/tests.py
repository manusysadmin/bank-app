from .models import CustomUser
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate, APIClient


class AuthTestCase(APITestCase):

    def setUp(self):
        self.username = "test-user"
        self.password = "testpassword"
        self.user = CustomUser.objects.create_user(username=self.username,
                                                   password=self.password)
        self.user.save()

    def test_login_and_jwt(self):
        response = self.client.post("/api/login", {'username': 'test-user',
                                                   'password': 'testpassword'}, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in response.data)
        self.assertTrue('refresh' in response.data)


class UserCreateTestCase(APITestCase):

    def test_usercreate(self):
        data = {"username": "testcase", "password": "testpassword"}

        response = self.client.post("/api/register", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


# Create your tests here.
