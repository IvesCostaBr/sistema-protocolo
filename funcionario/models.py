from django.db import models
from setor.models import Setor

# Create your models here.

class Funcionario(models.Model):
    nome_completo = models.CharField(
        max_length=90)

    cpf = models.CharField(
        max_length=15)

    data_nascimento = models.DateField(
        null=True, blank=True)

    status_empresa = models.CharField(
        max_length=20)

    setor = models.ForeignKey(Setor, blank=True,  on_delete=models.PROTECT)
    
    def notify_cadastro(self):
        pass

    def __str__(self):
        return " ID:   "+str(self.id) + '|     NOME:' + str(self.nome_completo)

