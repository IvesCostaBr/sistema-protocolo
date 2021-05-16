# Generated by Django 3.2.2 on 2021-05-15 08:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=90)),
                ('cpf', models.CharField(max_length=15)),
                ('data_nascimento', models.DateField(blank=True, null=True)),
                ('status_empresa', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responsavel', models.CharField(max_length=50)),
                ('nome_setor', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Protocolo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('bio', models.CharField(blank=True, max_length=300)),
                ('data', models.DateField(blank=True, default=datetime.datetime(2021, 5, 15, 8, 9, 29, 280297))),
                ('data_final', models.DateField()),
                ('file', models.FileField(blank=True, null=True, upload_to='media/')),
                ('funcionario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='painel.funcionario')),
            ],
        ),
        migrations.AddField(
            model_name='funcionario',
            name='setor',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.PROTECT, to='painel.setor'),
        ),
    ]
