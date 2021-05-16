from django.shortcuts import render
from django.views.generic import TemplateView


class SetorConfigHome(TemplateView):
    template_name = 'setor_config_home.html'


