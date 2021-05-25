# -*- coding: utf-8 -*-

# Python
from __future__                 import unicode_literals
from datetime                   import datetime

# Django
from django.db                  import models
from django.utils.translation   import ugettext_lazy as _

# Custom
from core.erp.models.client     import Client

class Sale(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_joined = models.DateField(default=datetime.now)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return 'Client name: {}'.format(self.client.name)
    
    class Meta:
        verbose_name = 'Sale'
        verbose_name_plural = 'Sales'
        ordering = ['id']
    
