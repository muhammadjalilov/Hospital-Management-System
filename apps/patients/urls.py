from django.urls import path

from apps.patients.views import PatientCreateAPIView, PatientListAPIView

app_name = 'patients'
urlpatterns = [
    path('patient-create/', PatientCreateAPIView.as_view(), name='patient_create'),
    path('patients/', PatientListAPIView.as_view(), name='patients'),
]
