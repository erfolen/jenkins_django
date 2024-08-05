from django.test import TestCase
from main.models import Categories, Products, Manufactures


class CategoriesModelTest(TestCase):
    def setUp(self):
        self.category = Categories.objects.create(
            meta_title="Test Meta Title",
            meta_description="Test Meta Description",
            meta_keywords="Test, Keywords",
            name="Test Category",
            description="Test Description",
            status=True,
            sort_order=1,
            url_slag="test-category",
            parent_id=0
        )

    def tearDown(self):
        Categories.objects.all().delete()

    def test_category_creation(self):
        self.assertIsInstance(self.category, Categories)
        self.assertEqual(self.category.__str__(), self.category.name)


class ManufacturesModelTest(TestCase):
    def setUp(self):
        self.manufacture = Manufactures.objects.create(
            meta_title="Test Meta Title",
            meta_description="Test Meta Description",
            meta_keywords="Test, Keywords",
            name="Test Manufacture",
            description="Test Description",
            status=True,
            sort_order=1,
            url_slag="test-manufacture"
        )

    def test_manufacture_creation(self):
        self.assertIsInstance(self.manufacture, Manufactures)
        self.assertEqual(self.manufacture.__str__(), self.manufacture.name)

    def tearDown(self):
        Manufactures.objects.all().delete()


class ProductsModelTest(TestCase):
    def setUp(self):
        self.category = Categories.objects.create(
            meta_title="Test Meta Title",
            meta_description="Test Meta Description",
            meta_keywords="Test, Keywords",
            name="Test Category",
            description="Test Description",
            status=True,
            sort_order=1,
            url_slag="test-category",
            parent_id=0
        )
        self.manufacture = Manufactures.objects.create(
            meta_title="Test Meta Title",
            meta_description="Test Meta Description",
            meta_keywords="Test, Keywords",
            name="Test Manufacture",
            description="Test Description",
            status=True,
            sort_order=1,
            url_slag="test-manufacture"
        )
        self.product = Products.objects.create(
            meta_title="Test Meta Title",
            meta_description="Test Meta Description",
            meta_keywords="Test, Keywords",
            name="Test Product",
            description="Test Description",
            status=True,
            sort_order=1,
            url_slag="test-product",
            article="TP12345",
            price=100.00,
            discount=10.00,
            quantity=50,
            category=self.category,
            manufacture=self.manufacture
        )
    def tearDown(self):
        Products.objects.all().delete()
        Categories.objects.all().delete()
        Manufactures.objects.all().delete()

    def test_product_creation(self):
        self.assertIsInstance(self.product, Products)
        self.assertEqual(self.product.__str__(), self.product.name)
        self.assertEqual(self.product.category, self.category)
        self.assertEqual(self.product.manufacture, self.manufacture)
        self.assertEqual(self.product.price, 100.00)
        self.assertEqual(self.product.discount, 10.00)
        self.assertEqual(self.product.quantity, 50)
