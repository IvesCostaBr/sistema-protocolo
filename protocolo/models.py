from django.db import models
from funcionario.models import Funcionario
from datetime import datetime
# Create your models here.

class Protocolo(models.Model):
    funcionario = models.ForeignKey(Funcionario, null=True, on_delete=models.DO_NOTHING)
    titulo = models.CharField(max_length=50)
    bio = models.CharField(max_length=300, blank=True)
    data =  models.DateField(default=datetime.now(), blank=True)
    data_final =  models.DateField(blank=True, null=True)
    file =  models.FileField(upload_to='', blank=True, null=True)

    def enviando_protocolo(self):
        return 'enviando protocolo'

    def __str__(self):
        return str(self.id) + '   ' + str(self.funcionario)
    