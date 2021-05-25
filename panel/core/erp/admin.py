# -*- coding: utf-8 -*-

# Django
from django.contrib import admin

# Custom
from core.erp.models.category       import Category
from core.erp.models.client         import Client
from core.erp.models.detail_sale    import DetailSale
from core.erp.models.product        import Product
from core.erp.models.sale           import Sale


# Register your models here.
admin.site.register(Category)
admin.site.register(Client)
admin.site.register(DetailSale)
admin.site.register(Product)
admin.site.register(Sale)