from django.forms import ModelForm
from .models import Funcionario

class FuncionarioForm(ModelForm):
    class Meta:
        model = Funcionario
        fields = ('nome_completo','cpf', 
        'data_nascimento', 'setor','status_empresa')