# -*- coding: utf-8 -*-

# Python
from __future__                 import unicode_literals
from datetime                   import datetime

# Django
from django.db                  import models
from django.utils.translation   import ugettext_lazy as _
from django.forms               import model_to_dict
from panel.settings             import STATIC_URL


# Custom 
from core.erp.models.category   import  Category


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name=_(u'Name'), unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/%Y/%m', null=True, blank=True, default='default/empty.png')
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    date_update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def toJson(self): #devuelve un diccionario con todo los datos, tambien puedo usar un exclude 
        item = model_to_dict(self)#convierte en diccionario los campos
        return item
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['id']
