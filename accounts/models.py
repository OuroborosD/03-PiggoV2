from django import db
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class CustomUser(AbstractUser):
    vencimento_cartao = models.SmallIntegerField(default=0)

    class Meta:
        db_table = 'User'

    def __str__(self):
        return  f'{self.username}'
