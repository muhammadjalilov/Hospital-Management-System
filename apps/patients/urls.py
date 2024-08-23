from django.urls import path

from apps.patients.views import PatientCreateAPIView, PatientListAPIView, PatientRetrieveUpdateAPIView

app_name = 'patients'
urlpatterns = [
    path('patient-create/', PatientCreateAPIView.as_view(), name='patient_create'),
    path('patients/', PatientListAPIView.as_view(), name='patients'),
    path('patient/<int:pk>/', PatientRetrieveUpdateAPIView.as_view(), name='patient'),
]
