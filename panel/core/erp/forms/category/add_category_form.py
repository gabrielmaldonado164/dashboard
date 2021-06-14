# -*- coding: utf-8 -*-

# Django
from django.forms import ModelForm
from django.forms import Textarea


# Custom
from core.erp.models.category   import Category

class CategoryForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'


    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'description':Textarea(
                attrs = {
                    'rows':3,
                    'cols':3
                }
            )
        }

        exclude = ['user_creation', 'user_update']

    #test 
    def clean(self):
        cleaned = super().clean()
        if len(cleaned['name']) <= 50:
            pass
            #raise self.model.ValidationErrors('Validacion erronea')#errores personalisados por cualquier otra que quiera hacer
            #self.add_error('name', 'Faltan caracteres')# errores para cada componentes del form
        
        return cleaned
