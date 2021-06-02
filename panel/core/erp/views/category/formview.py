# -*- coding: utf-8 -*-

# Django
from django.views.generic import FormView
from django.http    import JsonResponse
from django.urls    import reverse_lazy


# Custom
from core.erp.models.category   import Category
from core.erp.forms.category.add_category_form  import CategoryForm

#La diferencia con el created es que uno crea y otro no, solo valida que los datos ingresados sean correctos a lo que se pide

class CategoryFormView(FormView):
    form_class = CategoryForm
    template_name = 'category/formview.html'
    success_url = reverse_lazy('category_list_view')

    def get_context_data(self, **kwargs):
        context = super(CategoryFormView, self).get_context_data(**kwargs)
        context['title'] = 'Form categoria'
        return context
    