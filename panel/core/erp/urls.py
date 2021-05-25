# -*- coding: utf-8 -*-

# Django
from django.contrib import admin
from django.urls import path

from core.erp.views.category.list   import lista


urlpatterns = [
    path('category/list/', lista)
]
