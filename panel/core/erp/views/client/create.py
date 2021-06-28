# -*- coding: utf-8 -*-

# Django
from django.db import models
from django.views.generic import ListView


# Custom
from core.erp.forms.product.add_product_form import ProductForm

class ClientListView(ListView):
    models=   ProductForm
    template_name = 'client/create.html'


    def dispatch(self, request: http.HttpRequest, *args: Any, **kwargs: Any) -> HttpResponseBase:
        return super().dispatch(request, *args, **kwargs)

    
    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']

        try:
            data = []
            if action == 'createClient':
                for i in ProductForm:
                    data.append(i.toJson())
            else:
                data['error'] = 'No se encontraron resultados correspondiente'
        except Exception as e:
            data['error'] = str(e)
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context['title'] = 'Clients'
        return context
        

