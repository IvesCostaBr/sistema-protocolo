from django.shortcuts import render, get_object_or_404, redirect
from .models import Funcionario
from .forms import FuncionarioForm
from django.views.generic import TemplateView


class FuncionarioConfigHome(TemplateView):
    template_name = 'funcionario_home_config.html'


def adicionar_func(request):
    form = FuncionarioForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('funcionario_home')
    return render(request, 'funcionario_form.html', {'form':form})

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

    return render(request, 'funcionario_form.html', {'form':form})


