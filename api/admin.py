from django.contrib import admin
from api.forms import ScheduleForm
from api.models import Appointment, Doctor, Schedule, ScheduleHours

# Register your models here.
admin.site.register(Doctor)
admin.site.register(ScheduleHours)
admin.site.register(Appointment)

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    form = ScheduleForm
