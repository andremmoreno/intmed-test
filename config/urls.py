from django.contrib import admin
from django.urls import path
from api.views import DoctorViewSet, ScheduleViewSet
from rest_framework import routers
from django.conf.urls import include

router = routers.DefaultRouter()
router.register(r'doctors', DoctorViewSet)
router.register(r'schedules', ScheduleViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
