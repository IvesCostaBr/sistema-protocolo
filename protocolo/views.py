from django.shortcuts import render, redirect
from .models import Protocolo
from django.views.generic import TemplateView, CreateView

from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class ProtocoloConfigHome(LoginRequiredMixin, PermissionRequiredMixin,TemplateView):
    template_name = 'protocolo_config_home.html'
    permission_required = ('funcionario.rh_acess')
#TODO:Deve ser refeito um refactor ultilizando forms.Form para setar como valor padrão do protocolo o usuario da sessão.funcionario
class ProtocoloCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ('funcionario.gerar_protocolos')
    model = Protocolo
    fields = ('funcionario', 'titulo', 'bio', 'data', 'data_final','file')
    success_url = reverse_lazy('protocolo_home')
class EditarProtocolo(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ('funcionario.gerar_protocolos')
    model = Protocolo
    fields = ('funcionario', 'titulo', 'bio', 'data', 'data_final','file')

class DeleteProtocolo(LoginRequiredMixin, PermissionRequiredMixin,DeleteView):
    permission_required = ('funcionario.rh_acess')
    model = Protocolo
    success_url = reverse_lazy('protocolo_home')


def show_protocol(request): 
    if Protocolo.objects.select_related('funcionario').exists():
        return render(request, 'list_protocol.html',{'list_pro':Protocolo.objects.select_related('funcionario')} )
    return redirect('protocolo_home')
