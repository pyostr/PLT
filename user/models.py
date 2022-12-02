from django.contrib.auth.models import User
from django.db import models

from abstraction.models import AbstractModel


class AbstractUser(AbstractModel):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователь'

    user = models.OneToOneField(
        verbose_name='Пользователь',
        to=User,
        on_delete=models.CASCADE)

