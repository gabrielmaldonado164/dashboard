# -*- coding: utf-8 -*-


# Django
from django.db import models
from core.erp.forms.category.add_category_form import CategoryForm
from django.forms               import ModelForm, fields

# Custom
from core.erp.models.client     import Client

class ClientForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
    
    class Meta:
        model = Client
        exclude = ['date_update']
