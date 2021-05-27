# -*- coding: utf-8 -*-

# Django
from django.views.generic import DeleteView
from django.http import JsonResponse
from django.urls    import reverse_lazy


# Custom
from core.erp.models.category   import Category
from core.erp.forms.category.add_category_form  import CategoryForm

class CategoryDeleteView(DeleteView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/delete.html'
    success_url = reverse_lazy('category_list_view')