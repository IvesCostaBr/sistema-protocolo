from django.db import models
from datetime import datetime
from django.db.models import signals
from django.dispatch import receiver
# Create your models here.

class Contato(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=13)
    message = models.TextField(max_length=300)

    def send_email(self):
        return 'email enviado'

    def __str__(self):
        return self.nome + self.email + self.phone + self.message


#@receiver(signals.post_delete, sender=Protocolo)
#def send_email_admin(sender, instance, **kwargs):
#    c = instance.enviando_protocolo()
#    print(c)
    