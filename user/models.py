from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    created = models.TimeField(auto_now_add=True)

    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
