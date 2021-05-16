# Generated by Django 3.2.2 on 2021-05-15 19:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('painel', '0003_auto_20210515_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='setor',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='painel.setor'),
        ),
        migrations.AlterField(
            model_name='protocolo',
            name='data',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 5, 15, 19, 42, 4, 278240)),
        ),
    ]
