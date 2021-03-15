from .models import CustomUser
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate

class UserCreateTestCase(APITestCase):

    def test_usercreate(self):
        data = {"username": "testcase", "password": "testpassword"}

        response = self.client.post("/api/register", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


# Create your tests here.
