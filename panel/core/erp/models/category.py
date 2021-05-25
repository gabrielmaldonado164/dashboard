# -*- coding: utf-8 -*-

# Python
from __future__                 import unicode_literals



# Django
from django.db                  import models
from django.utils.translation   import ugettext_lazy as _




class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name=_(u'Name'), unique= True)

    def __str__(self):
        return 'Name: {}'.format(self.name)
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'
        ordering = ['id']

