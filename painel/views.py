from django.shortcuts import render
from .models import  Contato
from django.views.generic import TemplateView
from rest_framework import viewsets, permissions, authentication
from .Serializer import ContatoSerializer



#CBVS
#TODO:Consertar forma de inserção de dados ultilizando POST
class HomepagePainelMaster(TemplateView):
    template_name = 'painel/painel_home.html'


#TODO:API AREA 
#TODO: Criar permissões para acessar a api
class ContatoViewSet(viewsets.ModelViewSet):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer
  
