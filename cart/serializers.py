from rest_framework import serializers
from .models import Cart, CartItem
from main.serializers import ProductSerializer
from main.models import Products


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity']


class CartSerializers(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items', 'create', 'update']


class AddCartSerializers(serializers.ModelSerializer):
    product_id = serializers.IntegerField()

    class Meta:
        model = CartItem
        fields = ['product_id', 'quantity']

    def validate_product_id(self, value):
        try:
            Products.objects.get(id=value)
        except Products.DoesNotExits:
            raise serializers.ValidationError('Данного товара не существует')
        return value

    def create(self, validated_data):
        cart = self.context['cart']
        product = Products.objects.get(id=validated_data['product_id'])
        quantity = validated_data['quantity']

        # Проверка существует ли товар в корзине
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={'quantity': quantity}
        )

        if not created:
            cart_item.quantity += quantity
            cart_item.save()
        return cart_item



