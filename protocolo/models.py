from django.db import models
from funcionario.models import Funcionario
from datetime import datetime
from django.db.models import Count, Min, Max, F, Avg
from django.template.loader import render_to_string


from django.core.mail import send_mail, mail_admins
from django.db.models import signals
from django.dispatch import receiver
# Create your models here.

class ProtocoloManager(models.Manager):
    def total(self):
        return self.all().aggregate(Count('id'))['id__count']

class Protocolo(models.Model):
    funcionario = models.ForeignKey(Funcionario, null=True, on_delete=models.DO_NOTHING)
    titulo = models.CharField(max_length=50)
    bio = models.CharField(max_length=300, blank=True)
    data =  models.DateField(default=datetime.now(), blank=True)
    data_final =  models.DateField(blank=True, null=True)
    file =  models.FileField(upload_to='', blank=True, null=True)

    objects = ProtocoloManager()


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        data = {
                'funcionario': self.funcionario,
                'protocolo': self.id,
                'titulo':self.titulo, 
                'data': self.data,
            }
        html_email = render_to_string('protocolo/emails/email.html', data)
        plain_text = render_to_string('protocolo/emails/email.txt', data)

        send_mail(
                    f'Protocolo de Nº: {self.id} Criado.',
                    plain_text,
                    'no-response@cerberussistem.com.br',
                    [str(self.funcionario.setor.email),
                    str(self.funcionario.user.email)],
                    html_message=html_email,
                )
        mail_admins(
                    f'Protocolo de Nº: {self.id} Criado.(ADMIN EMAIL)',
                    plain_text,
                    html_message=html_email,
                )

    def __str__(self):
        return str(self.id) + '   ' + str(self.funcionario)
    
#@receiver(signals.post_save, sender=Protocolo)
#def hook_email(sender, instance, **kwargs):
#    instance.notificar_setor()