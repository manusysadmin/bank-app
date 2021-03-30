from bankapp.models import CustomUser, Product
from rest_framework import status
from rest_framework.test import APITestCase, APIClient


class UserTestCases(APITestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(username="test-user", password="testpassword")
        self.user.save()

        self.superuser = CustomUser.objects.create_superuser(username="test-admin", password="testpassword")
        self.superuser.save()

    def test_can_register_new_user(self):
        response = self.client.post("/api/register", {"username": "test-user-reg", "password": "testpassword"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 3)

    def test_can_login_registered_user(self):
        response = self.client.post("/api/login", {"username": "test-user", "password": "testpassword"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in response.data)
        self.assertTrue('refresh' in response.data)
        client = APIClient()
        client.logout()

    def test_can_get_user(self):
        login_response = self.client.post("/api/login", {"username": "test-admin", "password": "testpassword"})
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + login_response.data['access'])
        response = client.get("/api/manage/users/1")
        # TODO: add assertion

    def test_can_delete_user(self):
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

    def test_can_create_product_as_admin(self):
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

    def test_can_not_create_product_as_anon_user(self):
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

    def test_can_view_product_detail_as_admin(self):
        client = APIClient()
        login_response = self.client.post("/api/login", {'username': 'test-admin',
                                                         'password': 'testpassword'}, format='json')
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + login_response.data['access'])
        response = client.get("/api/manage/products/test-product")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_not_view_product_detail_as_anon_user(self):
        client = APIClient()
        login_response = self.client.post("/api/login", {'username': 'test-user',
                                                         'password': 'testpassword'}, format='json')
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + login_response.data['access'])
        response = client.get("/api/manage/products/test-product")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_can_update_product_as_admin(self):
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

    def test_can_not_update_product_as_anon_user(self):
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

    def test_can_delete_product_as_admin(self):
        client = APIClient()
        login_response = self.client.post("/api/login", {'username': 'test-admin',
                                                         'password': 'testpassword'}, format='json')
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + login_response.data['access'])
        response = client.delete("/api/manage/products/test-product")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)

    def test_can_not_delete_product_as_anon_user(self):
        client = APIClient()
        login_response = self.client.post("/api/login", {'username': 'test-user',
                                                         'password': 'testpassword'}, format='json')
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + login_response.data['access'])
        response = client.delete("/api/manage/products/test-product")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
