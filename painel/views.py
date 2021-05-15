from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import FuncionarioForm
from .models import Funcionario
from django.views.generic import TemplateView
#from django.urls import reversy_lazy
# Create your views here.

#CBVS

class Homepage(TemplateView):
    template_name = 'painel/painel_home.html'


#FBVS

def adicionar_func(request):
    form = FuncionarioForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('painel_home')
    return render(request, 'gestao.html', {'form':form})

def mostar_funcionarios(request):
    
    cadastros = Funcionario.objects.all()
    
    return render(request, 'cadastro_view.html', {'cadastros':cadastros})

def remove_funcionario(request, id):
    func = get_object_or_404(Funcionario, id=id)
    if request.method == 'POST':
        func.delete()
        return redirect('painel_home' )
    
    return render(request, 'confirm_delete.html', {'funcionario':func})


def edit_funcionarios(request, id):
    func = get_object_or_404(Funcionario, id=id)
    form = FuncionarioForm(request.POST or None, instance=func)

    if form.is_valid():
        form.save()
        return redirect('funcionario_view')

    return render(request, 'gestao.html', {'form':form})
