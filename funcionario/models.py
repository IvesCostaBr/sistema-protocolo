from django.db import models
from setor.models import Setor
from django.contrib.auth.models import User
from django.db.models import signals
from django.dispatch import receiver

# Create your models here.

class Funcionario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    nome_completo = models.CharField(
        max_length=90)

    cpf = models.CharField(
        max_length=15)

    data_nascimento = models.DateField(
        null=True, blank=True)

    status_empresa = models.CharField(
        max_length=20)

    setor = models.ForeignKey(Setor, blank=True,  on_delete=models.PROTECT)
    class Meta:
        permissions =(
            ('gerar_protocolos', 'user can create new protocol'),
            ('rh_acess', 'Acessos de RH no sistema CRUD'),
        )


    def notify_cadastro(self):
        print('email enviado para:' ,self.setor.email )

    def __str__(self):
        return " ID:   "+str(self.id) + '|     NOME:' + str(self.nome_completo)



@receiver(signals.post_save, sender=Funcionario)
def disparador_emails(sender, instance, **kwargs):
    return instance.notify_cadastro()