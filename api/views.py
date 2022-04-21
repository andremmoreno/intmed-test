from datetime import date
import sched
from django.http import Http404
from django.db.models import Count
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Appointment, Doctor, Schedule, ScheduleHours
from api.serializers import AppointmentSerializer, DoctorSerializer, ScheduleSerializer

class DoctorView(APIView):
    def get(self, request):
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        

class ScheduleView(APIView):
    def get(self, request):
        schedules = Schedule.objects.filter(dia__gte=date.today())
        appointments = Appointment.objects.filter(dia__gte=date.today())

        qs1 = schedules.values_list('dia', 'horarios', 'medico')
        qs2 = appointments.values_list('dia', 'horario', 'medico')
        qs3 = qs1.intersection(qs2)

        for item in qs3:
            agenda = schedules.filter(dia=item[0], medico=item[2]).first()
            agenda.horarios.remove(item[1])
        
        serializer = ScheduleSerializer(schedules, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AppointmentView(APIView):
    def get(self, request):
        appointments = Appointment.objects.filter(dia__gte=date.today())\
            .order_by('dia', 'horario')

        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
      
    def post(self, request):
        schedules = Schedule.objects.filter(dia__gte=date.today())
        appointments = Appointment.objects.filter(dia__gte=date.today())

        qs1 = schedules.values_list('dia', 'horarios', 'medico')
        qs2 = appointments.values_list('dia', 'horario', 'medico')
        qs3 = qs1.intersection(qs2)

        for item in qs3:
            agenda = schedules.filter(dia=item[0], medico=item[2]).first()
            agenda.horarios.remove(item[1])    
        try:
            marcacao = schedules.get(id=request.data['agenda_id'])
        except:
            return Response('Agenda não disponível', status=status.HTTP_400_BAD_REQUEST)
        
        hour = ScheduleHours.objects.get(horario=request.data['horario']).id
        if marcacao.horarios.filter(id=hour):
            serializer = AppointmentSerializer(
                data={
                    'medico': marcacao.medico.id,
                    'dia': marcacao.dia,
                    'horario': hour,
                })
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response('Horário não disponível', status=status.HTTP_400_BAD_REQUEST)
        


class AppointmentDetailsView(APIView):
    def get_object(self, pk):
        try:
            return Appointment.objects.get(pk=pk)
        except Appointment.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        appointment = self.get_object(pk)
        serializer = AppointmentSerializer(appointment)

        return Response(serializer.data)
      
    def delete(self, request, pk):
        appointment = self.get_object(pk)

        if appointment.dia < date.today():
            return Response('Consulta não pode ser desmarcada',status=405)

        appointment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)