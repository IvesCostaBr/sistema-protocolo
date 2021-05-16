from django.forms import ModelForm
from .models import Funcionario
from django import forms



class FuncionarioForm(ModelForm):


    nome_completo = forms.CharField(
        label='Nome Completo:', widget=forms.TextInput(
            attrs={'class': 'form-control',
                    'type': 'text',
                    'name': 'nome_completo',
                }
        )
    )
    cpf = forms.CharField(
        label='CPF:', widget=forms.TextInput(
            attrs={'class': 'form-control',
                    'type': 'text',
                    'name': 'cpf',
                }
        )
    )
    data_nascimento = forms.CharField(
        label='Data de Nascimento:', widget=forms.DateInput(
            attrs={'class': 'form-control',
                    'type': 'date',
                    'name': 'dt_nascimento',
                }
        )
    )
    setor = forms.CharField(
        label='Setor:', widget=forms.TextInput(
            attrs={'class': 'form-control',
                    'type': 'text',
                    'name': 'setor',
                }
        )
    )
    status_empresa= forms.CharField(
        label='Status:', widget=forms.TextInput(
            attrs={'class': 'form-control',
                    'name': 'status',
                }
        )
    )

    class Meta:
        model = Funcionario
        fields = ('nome_completo', 'cpf', 'data_nascimento', 'setor', 'status_empresa')