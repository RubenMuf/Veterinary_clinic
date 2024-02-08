from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True, null=True,verbose_name='Фотография') # по идее должно автоматически после миграции создаться папка медея для сохранения фотографий
    date_birth = models.DateTimeField(blank=True, null=True, verbose_name='Дата рождения')