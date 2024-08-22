from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from apps.doctor.models import Doctor, Specialities
from apps.patients.models import Patient
from apps.shared.models import BaseModel
from apps.users.models import User


class Appointment(BaseModel):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    datetime = models.DateTimeField()
    bunk = models.BooleanField(default=False)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.patient.id} {self.doctor.id}"


class Invoice(BaseModel):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='invoices')
    service_description = models.TextField(
        default="Invoice Description\nProject Name: [Your Project Name]\nClient: [Client Name]\nDate: [Invoice Date]\nInvoice Number: [Invoice Number]")
    paid = models.BooleanField(default=False)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)


class Pharmacy(BaseModel):
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=512)
    phone_number = PhoneNumberField()


class Prescription(BaseModel):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='prescriptions')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='prescriptions')
    medication_name = models.CharField(max_length=512)
    advice = models.TextField(blank=True, null=True)
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE, related_name='patients', null=True)
