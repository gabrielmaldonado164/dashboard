# -*- coding: utf-8 -*-

# Python
from __future__                 import unicode_literals
from datetime                   import datetime

# Django
from django.db                  import models
from django.utils.translation   import ugettext_lazy as _

# Custom
from core.erp.models.sale       import Sale
from core.erp.models.product    import Product


class DetailSale(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    amount = models.IntegerField(default=0)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return 'Name product: {}'.format(self.product.name)

    class Meta:
        verbose_name = 'DetailSale'
        verbose_name_plural = ' Sales details'
        ordering = ['id']