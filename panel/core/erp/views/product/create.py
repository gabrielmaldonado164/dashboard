# -*- coding: utf-8 -*-

# Django
from django.views.generic                       import CreateView
from django.http                                import JsonResponse
from django.urls                                import reverse_lazy
from django.contrib.auth.mixins                 import LoginRequiredMixin

# Custom
from core.erp.models.product                     import Product
from core.erp.forms.product.add_product_form     import ProductForm

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/create.html'
    success_url = reverse_lazy('product_list_view')

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
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super(ProductCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Producto'
        return context
    