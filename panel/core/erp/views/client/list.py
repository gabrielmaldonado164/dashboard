# -*- coding: utf-8 -*-


# Django
from django.db import models
from django.shortcuts               import render
from django.http                    import JsonResponse
from django.utils.decorators        import method_decorator
from django.views.decorators.csrf   import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins     import LoginRequiredMixin
from django.views.generic           import TemplateView


# Custom
from core.erp.models.client        import Client

class ClientListView(TemplateView):
    models = Client
    template_name  = 'client/list.html'
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}

        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Client.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'No se encontraron resultados'
        except  Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
    
    def get_context_data(self, **kwargs):
      context =  super().get_context_data(**kwargs)
      context['title'] = 'Clients'
      return context
         


