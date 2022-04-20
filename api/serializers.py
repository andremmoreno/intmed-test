from rest_framework import serializers
from api.models import Doctor, Schedule

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'nome', 'crm', 'email']

class ScheduleSerializer(serializers.ModelSerializer):
    medico = DoctorSerializer()
    class Meta:
        model = Schedule
        fields = ['id', 'medico', 'dia', 'horarios']