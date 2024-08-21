from django.urls import path

from apps.appointments.views import AppointmentCreateAPIView, AppointmentListAPIView, UnconfirmedAppointmentListAPIView, \
    ConfirmedAppointmentListAPIView

app_name = 'appointments'
urlpatterns = [
    path('create/', AppointmentCreateAPIView.as_view(), name='create_appointment'),
    path('', AppointmentListAPIView.as_view(), name='appointments_list'),
    path('unconfirmed-appointments/', UnconfirmedAppointmentListAPIView.as_view(), name='unconfirmed_appointments'),
    path('confirmed-appointments/', ConfirmedAppointmentListAPIView.as_view(), name='confirmed_appointments'),
]
