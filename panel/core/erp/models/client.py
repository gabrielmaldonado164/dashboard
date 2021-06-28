# -*- coding: utf-8 -*-

# Python
from __future__                 import unicode_literals
from datetime                   import datetime

# Django
from django.db                  import models
from django.utils.translation   import ugettext_lazy as _
from django.forms               import model_to_dict

class Client(models.Model):
    names = models.CharField(max_length=150, verbose_name=_(u'Names'))
    surnames = models.CharField(max_length=150, verbose_name=_(u'Surnames'))
    address = models.CharField(max_length=150,verbose_name=_(u'Address'), null=True, blank=True)
    date_update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Names: {}'.format(self.names)
    
    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
        ordering = ['id']


