from django.urls import path

from apps.hospital.views import HospitalListAPIView, HospitalRetrieveAPIView

app_name = 'hospital'
urlpatterns = [
    path('',HospitalListAPIView.as_view(),name='hospitals'),
    path('<int:pk>/',HospitalRetrieveAPIView.as_view(),name='hospital'),
]