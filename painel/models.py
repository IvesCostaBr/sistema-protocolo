from django.db import models

# Create your models here.

class Funcionario(models.Model):
    nome_completo = models.CharField(
        max_length=90)

    cpf = models.CharField(
        max_length=15)

    data_nascimento = models.DateField(
        null=True, blank=True)

    setor = models.CharField(
        max_length=30)

    status_empresa = models.CharField(
        max_length=20)


    def notify_cadastro(self):
        pass

    def __str__(self):
        return str(self.id) + '   ' + str(self.nome_completo)
    