from django.urls import path

from apps.appointments.views import AppointmentCreateAPIView, AppointmentListAPIView, UnconfirmedAppointmentListAPIView, \
    ConfirmedAppointmentListAPIView, ChangeStatusAppointments, PrescriptionCreateListAPIView, InvoiceListAPIView

app_name = 'appointments'
urlpatterns = [
    path('create/', AppointmentCreateAPIView.as_view(), name='create_appointment'),
    path('', AppointmentListAPIView.as_view(), name='appointments_list'),
    path('unconfirmed-appointments/', UnconfirmedAppointmentListAPIView.as_view(), name='unconfirmed_appointments'),
    path('confirmed-appointments/', ConfirmedAppointmentListAPIView.as_view(), name='confirmed_appointments'),
    path('change-status-appointments/<int:pk>/', ChangeStatusAppointments.as_view(), name='change_status_appointments'),
    path('prescription/', PrescriptionCreateListAPIView.as_view(), name='prescription'),
    path('invoices/', InvoiceListAPIView.as_view(), name='invoices'),
]
