from django.urls import path

from apps.patients.views import PatientCreateAPIView

app_name = 'patients'
urlpatterns = [
    path('patient-create/', PatientCreateAPIView.as_view(), name='patient_create')
]
