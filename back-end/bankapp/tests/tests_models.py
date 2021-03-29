from django.test import TestCase
from bankapp.models import CustomUser, Product


class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.product = Product.objects.create(
            name="Test Product",
            age=['JUNIOR'],
            student=False,
            income=['NO_INCOME']
        )

    def test_has_information_fields(self):
        self.assertIsInstance(self.product.name, str)
        self.assertIsInstance(self.product.age, list)
        self.assertIsInstance(self.product.student, bool)
        self.assertIsInstance(self.product.income, list)
        self.assertIsInstance(self.product.slug, str)

    def test_str(self):
        self.assertEqual(str(Product.objects.get(name="Test Product")), "Test Product")

    def test_get_absolute_url(self):
        product = Product.objects.get(name="Test Product")
        self.assertEqual(product.get_absolute_url(), '/api/manage/products/test-product')


class CustomUserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = CustomUser.objects.create(
            username="testuser",
            password="testpassword",
            role='USER'
        )

    def test_has_information_fields(self):
        self.assertIsInstance(self.user.username, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.role, str)
