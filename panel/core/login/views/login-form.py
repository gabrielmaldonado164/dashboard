# -*- coding: utf-8 -*-

# Django
from django.views.generic      import FormView
from django.urls               import reverse_lazy
from django.shortcuts          import redirect


class LoginForm(FormView):
    form_class = AuthenticationForm
    #success_url = reverse_lazy('category_list_view')
    #template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('category_list_view')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return redirect(self.success_url)


