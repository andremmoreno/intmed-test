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



class ScheduleHours(models.Model):
    HOURS_LIST = [
        ('10h', datetime.time(10, 0, 0)),
        ('11h', datetime.time(11, 0, 0)),
        ('13h', datetime.time(13, 0, 0)),
        ('14h', datetime.time(14, 0, 0)),
        ('15h', datetime.time(15, 0, 0)),
        ('16h', datetime.time(16, 0, 0)),
        ('17h', datetime.time(17, 0, 0)),
    ]
    horarios = models.CharField(
        max_length=3,
        choices=HOURS_LIST,
        default='10',
    )

class Schedule(models.Model):
    medico = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    dia = models.DateField(auto_created=True)
    horarios = models.ManyToManyField(ScheduleHours)
