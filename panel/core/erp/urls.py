# -*- coding: utf-8 -*-

# Django
from django.contrib import admin
from django.urls import path

from core.erp.views import test



urlpatterns = [
    path('prueba/',test),
]
