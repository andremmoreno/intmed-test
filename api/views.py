from rest_framework import viewsets
from api.models import Doctor, Schedule
from api.serializers import DoctorSerializer, ScheduleSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer