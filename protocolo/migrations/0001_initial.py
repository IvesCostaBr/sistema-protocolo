# Generated by Django 3.2.2 on 2021-05-16 04:45

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('funcionario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Protocolo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('bio', models.CharField(blank=True, max_length=300)),
                ('data', models.DateField(blank=True, default=datetime.datetime(2021, 5, 16, 4, 45, 28, 745550))),
                ('data_final', models.DateField()),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('funcionario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='funcionario.funcionario')),
            ],
        ),
    ]
