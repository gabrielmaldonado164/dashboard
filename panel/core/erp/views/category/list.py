# -*- coding: utf-8 -*-

# Django
from django.shortcuts import render
from django.views.generic import ListView
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Custom
from core.erp.models.category   import Category

class CategoryListView(ListView):
    model = Category
    template_name = 'category/list.html/'
    context_object_name = 'categories'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = Category.objects.get(pk=request.POST['id']).toJson()
        except Exception as e:
            data ['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['title'] = 'Category list'
        return context
    


