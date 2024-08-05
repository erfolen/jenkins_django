from rest_framework import serializers
from .models import Products, Manufactures


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class ManufacturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufactures
        fields = '__all__'

