# -*- coding: utf-8 -*-

# Django
from django.views.generic import TemplateView

class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    