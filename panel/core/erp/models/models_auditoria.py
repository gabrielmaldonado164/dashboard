# -*- coding: utf-8 -*-

# Django    
from django.db      import models
from django.conf    import settings


class AuditoriaModel(models.Model):
    user_creation = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_creation', blank=True, null=True)
    date_creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    user_update = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_update', blank=True, null=True)
    date_update = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self) -> str:
        return super().__str__(self.user_creation)
     

    #este model no se va a crear como tabla, si no que se pueda agregar en otra tablas correspondiente para que lo puedan usar
    class Meta:
        abstract = True  #el atributo de abstract cumple con la funcion de que no se  genere como tabla