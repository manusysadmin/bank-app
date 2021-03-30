from bankapp.models import CustomUser, Product
from rest_framework import status
from rest_framework.test import APITestCase, APIClient


class UserTestCases(APITestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(username="test-user", password="testpassword")
        self.user.save()

        self.superuser = CustomUser.objects.create_superuser(username="test-admin", password="testpassword")
        self.superuser.save()

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
        # TODO: add assertion

    def test_user_delete(self):
        login_response = self.client.post("/api/login", {"username": "test-admin", "password": "testpassword"})
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + login_response.data['access'])
        response = client.delete("/api/manage/users/1")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(CustomUser.objects.count(), 2)


class ProductTestCasesAuthorized(APITestCase):

    def setUp(self):
        data = {"name": "Test Product",
                "age": ['JUNIOR'],
                "student": False,
                "income": ["NO_INCOME"]}
        self.superuser = CustomUser.objects.create_superuser(username="test-admin",
                                                             password="testpassword")
        self.superuser.save()

        self.user = CustomUser.objects.create_user(username='test-user', password='testpassword')
        self.user.save()

        self.product = Product.objects.create(name="Test Product", age=['JUNIOR'], student=False, income=["NO_INCOME"])
        self.product.save()

    def test_product_create(self):
        client = APIClient()
        login_response = self.client.post("/api/login", {'username': 'test-admin',
                                                         'password': 'testpassword'}, format='json')
        token = login_response.data['access']
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        data = {"name": "Test Product Auth",
                "age": ['JUNIOR'],
                "student": False,
                "income": ["NO_INCOME"]}
        response = client.post("/api/manage/products/add", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)

    def test_product_create_unauth(self):
        client = APIClient()
        login_response = self.client.post("/api/login", {'username': 'test-user',
                                                         'password': 'testpassword'}, format='json')
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + login_response.data['access'])
        data = {"name": "Test Product Unauth",
                "age": ['JUNIOR'],
                "student": False,
                "income": ["NO_INCOME"]}
        response = client.post("/api/manage/products/add", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Product.objects.count(), 1)
        client.logout()

    def test_product_detail_view(self):
        client = APIClient()
        login_response = self.client.post("/api/login", {'username': 'test-admin',
                                                         'password': 'testpassword'}, format='json')
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + login_response.data['access'])
        response = client.get("/api/manage/products/test-product")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_product_detail_view_unauth(self):
        client = APIClient()
        login_response = self.client.post("/api/login", {'username': 'test-user',
                                                         'password': 'testpassword'}, format='json')
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + login_response.data['access'])
        response = client.get("/api/manage/products/test-product")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_product_update_view(self):
        client = APIClient()
        product = Product.objects.get(name="Test Product")
        login_response = self.client.post("/api/login", {'username': 'test-admin',
                                                         'password': 'testpassword'}, format='json')
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + login_response.data['access'])
        response = client.put("/api/manage/products/test-product", {'name': 'Test Product Edited',
                                                                    'age': ['JUNIOR'],
                                                                    'student': False,
                                                                    'income': ['NO_INCOME']})
        product.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_product_update_view_unauth(self):
        client = APIClient()
        product = Product.objects.get(name="Test Product")
        login_response = self.client.post("/api/login", {'username': 'test-user',
                                                         'password': 'testpassword'}, format='json')
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + login_response.data['access'])
        response = client.put("/api/manage/products/test-product", {'name': 'Test Product Edited',
                                                                    'age': ['JUNIOR'],
                                                                    'student': False,
                                                                    'income': ['NO_INCOME']})
        product.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_product_delete_view(self):
        client = APIClient()
        login_response = self.client.post("/api/login", {'username': 'test-admin',
                                                         'password': 'testpassword'}, format='json')
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + login_response.data['access'])
        response = client.delete("/api/manage/products/test-product")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)

    def test_product_delete_view_unauth(self):
        client = APIClient()
        login_response = self.client.post("/api/login", {'username': 'test-user',
                                                         'password': 'testpassword'}, format='json')
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + login_response.data['access'])
        response = client.delete("/api/manage/products/test-product")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
