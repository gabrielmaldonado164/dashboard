# -*- coding: utf-8 -*-

# Django
from django.views.generic import UpdateView
from django.http import JsonResponse
from django.urls    import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Custom
from core.erp.models.category   import Category
from core.erp.forms.category.add_category_form  import CategoryForm

class CategoryEditView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/edit.html'
    success_url = reverse_lazy('category_list_view')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()#al ser un edit con datos por ajax, se tiene que tomar el objecto para poder instanciarlo y poder editar los datos
        return super().dispatch(request, *args, **kwargs)

    #puedo usar el post de esta manera con ajax  para editar
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
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
        context = super(CategoryEditView, self).get_context_data(**kwargs)
        context['title'] = 'Editar categoria'
        return context
    

