# -*- coding: utf-8 -*-

# Django
from django.shortcuts               import render
from django.views.generic           import ListView
from django.http                    import JsonResponse
from django.utils.decorators        import method_decorator
from django.views.decorators.csrf   import csrf_exempt
from django.contrib.auth.mixins     import LoginRequiredMixin

# Custom
from core.erp.models.product        import Product

class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'product/list.html/'
    context_object_name = 'products'
    

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['title'] = 'Listado de Producto'
        return context
    