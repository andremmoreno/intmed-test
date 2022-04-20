from datetime import date
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Appointment, Doctor, Schedule
from api.serializers import AppointmentSerializer, DoctorSerializer, ScheduleSerializer

class DoctorView(APIView):
    def get(self, request):
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        

class ScheduleView(APIView):
    def get(self, request):
        schedules = Schedule.objects.all()
        serializer = ScheduleSerializer(schedules, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AppointmentView(APIView):
    def get(self, request):
        appointments = Appointment.objects.all()
        result = [d for d in appointments if d.dia >= date.today()]
        result = sorted(result, key=lambda result: result.horario)
        result = sorted(result, key=lambda result: result.dia)
        serializer = AppointmentSerializer(result, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)