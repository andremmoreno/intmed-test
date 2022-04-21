from django.db import models
from django.core.validators import MaxValueValidator
import datetime

# Create your models here.
class Doctor(models.Model):
    nome = models.CharField('Médico', max_length=30, null=False, blank=False)
    crm = models.PositiveIntegerField('CRM', unique=True, validators=[MaxValueValidator(999999)], null=False)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Médico'



class ScheduleHours(models.Model):
    horario = models.TimeField(unique=True, null=False)
    def __str__(self):
        return str(self.horario)

    class Meta:
        verbose_name = 'Horário'

class Schedule(models.Model):
    medico = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=False)
    dia = models.DateField(auto_created=True, null=False, blank=False)
    horarios = models.ManyToManyField(ScheduleHours)

    def __str__(self):
        return str(self.medico) + ' - ' + str(self.dia)

    class Meta:
        verbose_name = 'Agenda'

class Appointment(models.Model):
    medico = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=False)
    dia = models.DateField(auto_created=True, null=False)
    horario = models.ForeignKey(ScheduleHours, on_delete=models.CASCADE, null=False)
    data_agendamento = models.DateTimeField(default=datetime.datetime.now, blank=True)

    def __str__(self):
        return str(self.dia) + ' - ' + str(self.horario)


    class Meta:
        verbose_name = 'Consulta'