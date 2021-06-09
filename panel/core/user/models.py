# -*- coding: utf-8 -*-

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser #llamo a la clase donde se encuentra el user

class User(AbstractUser):
    image = models.ImageField(upload_to='users/%Y/%m/%d', null=True, blank=True, default='default/avatar.png')
