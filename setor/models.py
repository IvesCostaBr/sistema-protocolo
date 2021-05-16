from django.db import models

# Create your models here.


class Setor(models.Model):
    responsavel =  models.CharField(max_length=50)
    nome_setor = models.CharField(max_length=30)
    email =  models.EmailField(max_length=50)

    def __str__(self):
        return str(self.nome_setor)
