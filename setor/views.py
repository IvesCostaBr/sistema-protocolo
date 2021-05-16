from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Setor
from django.views.generic import CreateView, ListView
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy

class SetorConfigHome(TemplateView):
    template_name = 'setor_config_home.html'

class CriarSetor(CreateView):
    model = Setor
    fields = ('responsavel','nome_setor', 'email')
    success_url = reverse_lazy('setor_config_home')

class ListarSetores(ListView):
    model = Setor

class DeleteSetor(DeleteView):
    model = Setor

class EditarSetor(UpdateView):
    model = Setor
    fields = ('responsavel','nome_setor', 'email')
    success_url = reverse_lazy('setor_config_home')




