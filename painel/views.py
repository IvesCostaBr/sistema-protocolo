from django.shortcuts import render, HttpResponse
from .forms import FuncionarioForm
from .models import Funcionario
# Create your views here.


def painel_home(request):
    return render(request, 'painel_home.html')

def adicionar_func(request):
    form = FuncionarioForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponse('Cadastro realizado')
    return render(request, 'gestao.html', {'form':form})