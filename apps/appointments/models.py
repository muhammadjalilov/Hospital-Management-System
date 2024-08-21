from django.db.models import ForeignKey, CASCADE, DateTimeField, TextField, DecimalField, CharField, Sum, BooleanField
from phonenumber_field.modelfields import PhoneNumberField

from apps.doctor.models import Doctor
from apps.patients.models import Patient
from apps.shared.models import BaseModel


class Appointment(BaseModel):
    patient = ForeignKey(Patient, on_delete=CASCADE, related_name='appointments')
    doctor = ForeignKey(Doctor, on_delete=CASCADE, related_name='appointments')
    datetime = DateTimeField(auto_now=True)
    status = BooleanField(default=False)


class Invoice(BaseModel):
    patient = ForeignKey(Patient, on_delete=CASCADE, related_name='invoices')
    service_description = TextField(blank=True, null=True)
    paid = BooleanField(default=False)
    cost = DecimalField(max_digits=10, decimal_places=2, default=0)

    def calculate_cost(self):
        return self.patient.appointments.doctor.speciality.cost

    def save(self, *args, **kwargs):
        self.cost = self.calculate_cost()
        super().save(*args, **kwargs)


class Pharmacy(BaseModel):
    name = CharField(max_length=256)
    address = CharField(max_length=512)
    phone_number = PhoneNumberField()


class Prescription(BaseModel):
    patient = ForeignKey(Patient, on_delete=CASCADE, related_name='prescriptions')
    medication_name = CharField(max_length=512)
    advice = TextField(blank=True, null=True)
    pharmacy = ForeignKey(Pharmacy, on_delete=CASCADE, related_name='patients',null=True)

