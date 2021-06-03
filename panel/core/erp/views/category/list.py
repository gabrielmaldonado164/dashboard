# -*- coding: utf-8 -*-

# Django
from django.shortcuts               import render
from django.views.generic           import ListView
from django.http                    import JsonResponse
from django.utils.decorators        import method_decorator
from django.views.decorators.csrf   import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins     import LoginRequiredMixin



# Custom
from core.erp.models.category        import Category

class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'category/list.html/'
    context_object_name = 'categories'
    

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    

    #Listando con datatable -> aumenta el rendimiento ya que no tiene que iterar con un for con las vista de django
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'list':
                data = []
                for i in Category.objects.all():
                    data.append(i.toJson())#lo guardo como una coleccion de diccionario, el toJson me convierte los datos  en dict
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data ['error'] = str(e)
        return JsonResponse(data, safe=False)# cuando se trabaja con coleccion de datos se pone el modo safe=false

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['title'] = 'Listado de Categorias'
        return context
    


