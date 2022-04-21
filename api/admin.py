from django.contrib import admin
from api.forms import ScheduleForm
from api.models import Appointment, Doctor, Schedule, ScheduleHours

# Register your models here.
admin.site.register(Doctor)
admin.site.register(ScheduleHours)

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    form = ScheduleForm

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    exclude = ('data_agendamento',)