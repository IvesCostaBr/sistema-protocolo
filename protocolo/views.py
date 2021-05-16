from django.shortcuts import render, redirect
from .models import Protocolo
from django.views.generic import TemplateView, CreateView

from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy



class ProtocoloConfigHome(TemplateView):
    template_name = 'protocolo_config_home.html'

class ProtocoloCreate(CreateView):
    model = Protocolo
    fields = ('funcionario', 'titulo', 'bio', 'data', 'data_final','file')
    success_url = reverse_lazy('protocolo_home')
class EditarProtocolo(UpdateView):
    model = Protocolo
    fields = ('funcionario', 'titulo', 'bio', 'data', 'data_final','file')

class DeleteProtocolo(DeleteView):
    model = Protocolo
    success_url = reverse_lazy('protocolo_home')


def show_protocol(request): 
    if Protocolo.objects.select_related('funcionario').exists():
        return render(request, 'list_protocol.html',{'list_pro':Protocolo.objects.select_related('funcionario')} )
    return redirect('protocolo_home')
