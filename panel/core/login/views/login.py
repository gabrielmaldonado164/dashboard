# -*- coding: utf-8 -*-

# Django
from django.contrib.auth.views import LoginView
from django.urls               import reverse_lazy
from django.shortcuts          import redirect



class LoginFormView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('home')
    

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('category_list_view')
        return super().dispatch(request, *args, **kwargs)



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar sesion'
        return context