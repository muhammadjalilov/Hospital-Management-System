from django.urls import path

from apps.hospital.views import HospitalListAPIView, DepartmentListAPIView

app_name = 'hospital'
urlpatterns = [
    path('',HospitalListAPIView.as_view(),name='hospitals'),
    path('departments/',DepartmentListAPIView.as_view(),name='hospitals'),
]