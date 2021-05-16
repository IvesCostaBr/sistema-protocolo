from django.shortcuts import render, redirect
from .models import  Contato
from django.views.generic import TemplateView
from rest_framework import viewsets, permissions, authentication
from .Serializer import ContatoSerializer
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin



#CBVS
#TODO:Consertar forma de inserção de dados ultilizando POST
class HomepagePainelMaster(LoginRequiredMixin, TemplateView):
    template_name = 'painel/painel_home.html'
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('funcionario.rh_acess'):
            return redirect('404_page')
        return super(HomepagePainelMaster, self).dispatch(request, *args, **kwargs)

def change_password(request):
    if request.method == 'POST':
        username = request.POST['username']
        new_password = request.POST['password']
        User.objects.get(username=username).set_password(new_password)
        return redirect('homepage')

    return render(request, 'change_password.html')

#TODO:API AREA 
#TODO: Criar permissões para acessar a api
class ContatoViewSet(viewsets.ModelViewSet):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer
  
