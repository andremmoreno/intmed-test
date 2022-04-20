from tabnanny import verbose
from django.db import models
from django.core.validators import MaxValueValidator
import datetime

# Create your models here.
class Doctor(models.Model):
    nome = models.CharField(max_length=30, null=False, blank=False)
    crm = models.PositiveIntegerField(unique=True, validators=[MaxValueValidator(999999)])
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Médico'



class ScheduleHours(models.Model):
    HOURS_LIST = [
        ('09:00', datetime.time(9, 0, 0)),
        ('10:00', datetime.time(10, 0, 0)),
        ('11:00', datetime.time(11, 0, 0)),
        ('13:00', datetime.time(13, 0, 0)),
        ('14:00', datetime.time(14, 0, 0)),
        ('15:00', datetime.time(15, 0, 0)),
        ('16:00', datetime.time(16, 0, 0)),
        ('17:00', datetime.time(17, 0, 0)),
    ]
    horario = models.CharField(
        max_length=5,
        choices=HOURS_LIST,
        unique=True,  
    )
    def __str__(self):
        return self.horario

    class Meta:
        verbose_name = 'Horário'

class Schedule(models.Model):
    medico = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    dia = models.DateField(auto_created=True)
    horarios = models.ManyToManyField(ScheduleHours)

class Appointment(models.Model):
    medico = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    dia = models.DateField(auto_created=True)
    horario = models.CharField(max_length=5, default='')
    data_agendamento = models.DateTimeField(default=datetime.datetime.now, blank=True)
