# -*- coding: utf-8 -*-

# Django
from django.contrib import admin
from django.urls import path

# Custom
from core.erp.views.category.list   import CategoryListView
from core.erp.views.category.create import CategoryCreateView
from core.erp.views.category.edit   import CategoryEditView
from core.erp.views.category.delete import CategoryDeleteView


urlpatterns = [
    path('category/list/', CategoryListView.as_view(), name='category_list_view'),
    path('category/add/', CategoryCreateView.as_view(), name='category_create_view'),
    path('category/edit/<int:pk>/', CategoryEditView.as_view(), name='category_edit_view'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete_view'),


]
