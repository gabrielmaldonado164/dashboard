# -*- coding: utf-8 -*-

# Django
from django.forms              import ModelForm

# Custom
from core.erp.models.product   import Product

class ProductForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'


    class Meta:
        model = Product
        fields = '__all__'


    #test 
    def clean(self):
        cleaned = super().clean()
        if len(cleaned['name']) <= 50:
            pass
            #raise self.model.ValidationErrors('Validacion erronea')#errores personalisados por cualquier otra que quiera hacer
            #self.add_error('name', 'Faltan caracteres')# errores para cada componentes del form
        
        return cleaned
