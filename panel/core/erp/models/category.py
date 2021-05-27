# -*- coding: utf-8 -*-

# Python
from __future__                 import unicode_literals

# Django
from django.db                  import models
from django.utils.translation   import ugettext_lazy as _
from django.forms import model_to_dict




class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name=_(u'Name'), unique= True)
    description = models.TextField(max_length=300, null=True, blank=True, verbose_name=_(u'Description'))

    def __str__(self):
        return self.name
    
    def toJson(self): #devuelve un diccionario con todo los datos, tambien puedo usar un exclude 
        item = model_to_dict(self)#convierte en diccionario los campos
        return item

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'
        ordering = ['id']

