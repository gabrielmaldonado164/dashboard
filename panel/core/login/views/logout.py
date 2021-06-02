# -*- coding: utf-8 -*-

# Django
from django.contrib.auth.views import LogoutView

class LogoutFormView(LogoutView):
    next_page = 'login_view'




#from django.contrib.auth import logout 

#class LogoutRedirect(RedirectView): No cierra la sesion solo hace un redir
    #pattern_name = 'login'}

    #def dispatch(self, request, *args, **kwargs):
        #logout(request) -> cierro sesion
        #return super().dispatch(request, *args, **kwargs)

