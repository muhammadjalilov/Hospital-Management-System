from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.doctor.views import DoctorRegisterAPIView, DoctorListAPIView, DoctorRetrieveAPIView

app_name = 'doctor'

urlpatterns = [
    path('register/', DoctorRegisterAPIView.as_view(), name='doctor_create'),
    path('list/', DoctorListAPIView.as_view(), name='doctor_list'),
    path('<int:pk>/', DoctorRetrieveAPIView.as_view(), name='doctor_retrieve'),
]
