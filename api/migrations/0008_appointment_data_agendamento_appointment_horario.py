# Generated by Django 4.0.4 on 2022-04-20 01:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_rename_hora_schedulehours_horario_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='data_agendamento',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='appointment',
            name='horario',
            field=models.CharField(default='', max_length=5),
        ),
    ]
