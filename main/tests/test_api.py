from django.urls import reverse
from django.utils.http import urlencode
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from main.models import Categories, Products, Manufactures
from main.serializers import ProductSerializer, ManufacturesSerializer


class MainApiTestCAse(APITestCase):
    def setUp(self):
        self.client = APIClient()
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

    def test_products_get(self):
        url = reverse('products-list')
        response = self.client.get(url)
        serializers_data = ProductSerializer([self.product_1, self.product_2], many=True).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializers_data, response.data)

    def test_product_get(self):
        url = reverse('product-detail', args=[self.product_1.pk])
        response = self.client.get(url)
        serializers_data = ProductSerializer(self.product_1).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializers_data, response.data)

    def test_search_get(self):
        url = reverse('product-search')
        query_params = {'name': 'Диван'}
        full_url = f"{url}?{urlencode(query_params)}"
        response = self.client.get(full_url)
        expected_products = Products.objects.filter(name__icontains='Диван')
        serializer_data = ProductSerializer(expected_products, many=True).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer_data, response.data)

    def test_manufactures_get(self):
        url = reverse('manufactures-list')
        response = self.client.get(url)
        serializers_data = ManufacturesSerializer([self.manufacture_1, self.manufacture_2], many=True).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializers_data, response.data)

