from rest_framework import serializers
from api.models import Appointment, Doctor, Schedule, ScheduleHours

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'nome', 'crm', 'email']

class ScheduleHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleHours
        fields = ['horario']

class ScheduleSerializer(serializers.ModelSerializer):
    medico = DoctorSerializer()
    horarios = serializers.SlugRelatedField(
      many = True,
      read_only = True,
      slug_field = 'horario'
    )
    class Meta:
        model = Schedule
        fields = ['id', 'medico', 'dia', 'horarios']

class AppointmentSerializer(serializers.ModelSerializer):
    medico = DoctorSerializer()
    class Meta:
        model = Appointment
        fields = ['id', 'medico', 'dia', 'horario', 'data_agendamento']