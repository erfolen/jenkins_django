from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Cart, CartItem
from main.models import Products
from .serializers import CartSerializers, AddCartSerializers, ProductSerializer


class CartView(generics.RetrieveAPIView):
    serializer_class = CartSerializers
    # permission_classes = [IsAuthenticated]

    def get_object(self):
        cart, created = Cart.objects_or_created(user=self.request.user)
        return cart


class AddCartItemView(generics.CreateAPIView):
    serializer_class = AddCartSerializers
    # permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        context['cart'] = cart
        return context

    def create(self, request, *args, **kwargs):
        context = self.get_serializer_context()
        serializer = self.get_serializer(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

