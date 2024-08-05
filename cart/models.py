from django.db import models
from user.models import User
from main.models import Products

# Create your models here.


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    create = models.TimeField(auto_now_add=True)
    update = models.TimeField(auto_now=True)

    def __str__(self):
        return f'Корзина {self.user.username}'


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f'В корзине {self.cart.id} -- {self.product.name} в количестве {self.quantity}'
