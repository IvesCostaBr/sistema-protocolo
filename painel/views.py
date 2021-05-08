from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import FuncionarioForm
from .models import Funcionario
# Create your views here.



#FBV
def painel_home(request):
    return render(request, 'painel_home.html')

def adicionar_func(request):
    form = FuncionarioForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('painel_home')
    return render(request, 'gestao.html', {'form':form})

def mostar_funcionarios(request):
    if request.method == 'POST':
        cadastros = Funcionario.objects.all()
    
    return render(request, 'cadastro_view.html', {'cadastros':cadastros})

def remove_funcionario(request, id):
    if request.method == 'POST':
        func = Funcionario.objects.get(id=id)
        func.delete()
        return redirect('painel_home')
    
    return render(request, 'confirm_delete.html')


def edit_funcionarios(request, id):
    func = get_object_or_404(Funcionario, id=id)
    form = FuncionarioForm(request.POST or None, instance=func)

    if form.is_valid():
        form.save()
        return redirect('funcionario_view')

    return render(request, 'gestao.html', {'form':form})
