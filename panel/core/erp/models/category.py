# -*- coding: utf-8 -*-

# Python
from __future__                         import unicode_literals

# Django
from django.db                          import models
from core.erp.models.models_auditoria   import AuditoriaModel
from django.utils.translation           import ugettext_lazy as _
from django.forms                       import model_to_dict
from crum                             import get_current_user






class Category(AuditoriaModel):
    name = models.CharField(max_length=150, verbose_name=_(u'Name'), unique= True)
    description = models.TextField(max_length=300, null=True, blank=True, verbose_name=_(u'Description'))

    def __str__(self):
        return self.name
    
    def toJson(self): #devuelve un diccionario con todo los datos, tambien puedo usar un exclude 
        item = model_to_dict(self)#convierte en diccionario los campos
        return item

    #para auditoria se sobreescribe el metodo save para poder obtener las peticions de los usuarios en session
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_update = user
        super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'
        ordering = ['id']

