# Generated by Django 4.0.4 on 2022-04-21 00:51

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, verbose_name='Médico')),
                ('crm', models.PositiveIntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(999999)], verbose_name='CRM')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
            options={
                'verbose_name': 'Médico',
            },
        ),
        migrations.CreateModel(
            name='ScheduleHours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario', models.TimeField(unique=True)),
            ],
            options={
                'verbose_name': 'Horário',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.DateField(auto_created=True)),
                ('horarios', models.ManyToManyField(to='api.schedulehours')),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.doctor')),
            ],
            options={
                'verbose_name': 'Agenda',
            },
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.DateField(auto_created=True)),
                ('data_agendamento', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('horario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.schedulehours')),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.doctor')),
            ],
            options={
                'verbose_name': 'Consulta',
            },
        ),
    ]
