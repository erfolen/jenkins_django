from datetime import timedelta, datetime

from django.test import TestCase

from main.models import Categories, Products, Manufactures
from main.serializers import ProductSerializer, ManufacturesSerializer


class MainSerializersTestCase(TestCase):
    def setUp(self):
        self.category_1 = Categories.objects.create(name='Диваны')
        self.product_1 = Products.objects.create(
            name='Угловой диван «Леруа» (2L.90.1R)', article='2L.90.1R', price=6772, quantity=10,
            category=self.category_1
        )
        self.product_2 = Products.objects.create(
            name='3-х местный диван «Ален 1»', article='Ален 1', price=2090, quantity=3,
            category=self.category_1
        )
        self.manufacture_1 = Manufactures.objects.create(name='Ани мебель')
        self.manufacture_2 = Manufactures.objects.create(name='Пинск Древ')

    def tearDown(self):
        Products.objects.all().delete()
        Categories.objects.all().delete()
        Manufactures.objects.all().delete()

    @staticmethod
    def delete_field(fields, data):
        if isinstance(fields, list):
            for field in fields:
                for item in data:
                    item.pop(field)
        else:
            data.pop(fields)

    def test_products(self):
        serializers_data = ProductSerializer([self.product_1, self.product_2], many=True).data
        self.delete_field(['created', 'update'], serializers_data)
        data = [
            {
                'id': self.product_1.id, 'meta_title': None, 'meta_description': None, 'meta_keywords': None,
                'name': 'Угловой диван «Леруа» (2L.90.1R)', 'description': None, 'status': True, 'sort_order': 0,
                'image': None, 'url_slag': None, 'article': '2L.90.1R', 'price': '6772.00',
                'discount': '0.00', 'quantity': 10, 'category': self.product_1.category.id, 'manufacture': None
            },
            {
                'id': self.product_2.id, 'meta_title': None, 'meta_description': None, 'meta_keywords': None,
                'name': '3-х местный диван «Ален 1»', 'description': None, 'status': True, 'sort_order': 0,
                'image': None, 'url_slag': None, 'article': 'Ален 1', 'price': '2090.00',
                'discount': '0.00', 'quantity': 3, 'category': self.product_1.category.id, 'manufacture': None
            }
        ]
        self.assertEqual(serializers_data, data)

    def test_manufactory(self):
        serializers_data = ManufacturesSerializer([self.manufacture_1, self.manufacture_2], many=True).data
        self.delete_field(['created', 'update'], serializers_data)
        data = [
            {
                'id': self.manufacture_1.id, 'meta_title': None, 'meta_description': None, 'meta_keywords': None, 'name': 'Ани мебель',
                'description': None, 'status': True, 'sort_order': 0, 'image': None, 'url_slag': None,
            },
            {
                'id': self.manufacture_2.id, 'meta_title': None, 'meta_description': None, 'meta_keywords': None, 'name': 'Пинск Древ',
                'description': None, 'status': True, 'sort_order': 0, 'image': None, 'url_slag': None
            }
        ]
        self.assertEqual(serializers_data, data)
