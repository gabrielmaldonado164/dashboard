# -*- coding: utf-8 -*-

# Django
from django.contrib import admin
from django.urls import path

# Custom
# Category
from core.erp.views.category.list     import CategoryListView
from core.erp.views.category.create   import CategoryCreateView
from core.erp.views.category.edit     import CategoryEditView
from core.erp.views.category.delete   import CategoryDeleteView
from core.erp.views.category.formview import CategoryFormView

# Product
from core.erp.views.product.list    import ProductListView
from core.erp.views.product.create  import ProductCreateView
from core.erp.views.product.delete  import ProductDeleteView
from core.erp.views.product.edit    import ProductEditView

# Client 
from core.erp.views.client.list     import ClientListView

# Home
from core.erp.views.dashboard.views     import DashboardView


urlpatterns = [
    # Category
    path('category/list/', CategoryListView.as_view(), name='category_list_view'),
    path('category/add/', CategoryCreateView.as_view(), name='category_create_view'),
    path('category/edit/<int:pk>/', CategoryEditView.as_view(), name='category_edit_view'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete_view'),
    path('category/formview/', CategoryFormView.as_view(), name='category_form_view'),

    # Product
    path('product/list/',  ProductListView.as_view(), name='product_list_view'),
    path('product/add/',  ProductCreateView.as_view(), name='product_create_view'),
    path('product/edit/<int:pk>/', ProductEditView.as_view(), name='product_edit_view'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete_view'),

    # Client
    path('client/list/', ClientListView.as_view(), name='client_list_view' ),


    # Home    
    path('dashboard/', DashboardView.as_view(), name='home',)
]
