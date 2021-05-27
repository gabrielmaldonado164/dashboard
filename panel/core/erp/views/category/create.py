# -*- coding: utf-8 -*-

# Django
from django.views.generic import CreateView
from django.http import JsonResponse
from django.urls    import reverse_lazy


# Custom
from core.erp.models.category   import Category
from core.erp.forms.category.add_category_form  import CategoryForm

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/create.html'
    success_url = reverse_lazy('category_list_view')

    #puedo usar el post de esta manera con ajax 
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                if form.is_valid():
                    form.save()
                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'No hay action con ese nombre'
        except Exception as e:
            data ['error'] = str(e)
        return JsonResponse(data, safe=False )
        

    def get_context_data(self, **kwargs):
        context = super(CategoryCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear categoria'
        return context
    