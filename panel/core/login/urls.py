# -*- coding: utf-8 -*-

# Django
from django.contrib import admin
from django.urls import path

# Custom
from core.login.views.login   import LoginFormView
from core.login.views.logout  import LogoutFormView


urlpatterns = [
    path('', LoginFormView.as_view(), name='login_view'),
    path('logout',LogoutFormView.as_view(), name='logout_view' ),
]
