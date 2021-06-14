# -*- coding: utf-8 -*-

# Django
from django.views.generic                       import DeleteView
from django.http                                import JsonResponse
from django.urls                                import reverse_lazy
from django.contrib.auth.mixins                 import LoginRequiredMixin

# Custom
from core.erp.models.product                    import Product
from core.erp.forms.product.add_product_form    import ProductForm

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    form_class = ProductForm
    template_name = 'product/delete.html'
    success_url = reverse_lazy('product_list_view')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()#al ser un edit con datos por ajax, se tiene que tomar el objecto para poder instanciarlo y poder editar los datos
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'delete':
                self.object.delete()
            else:
                data['error'] = 'No hay action con ese nombre'

        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super(ProductDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Eliminar  Producto'
        return context
    