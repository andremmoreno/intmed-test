from django.contrib import admin
from django.urls import path
from api.views import AppointmentView, DoctorView, ScheduleView
from rest_framework import routers
from django.conf.urls import include

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('medicos/', DoctorView.as_view()),
    path('agendas/', ScheduleView.as_view()),
    path('consultas/', AppointmentView.as_view()),
]
