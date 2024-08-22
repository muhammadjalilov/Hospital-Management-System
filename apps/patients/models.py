from django.db import models
from django.utils import timezone
from rest_framework.exceptions import ValidationError

from apps.doctor.models import Doctor
from apps.shared.models import BaseModel
from apps.users.models import User


class Patient(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient')

    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)


class RoomManager(models.Manager):
    def assign_room(self, patient, doctor, days=10):
        available_rooms = self.filter(patient__isnull=True)
        if available_rooms.count() == 0:
            raise ValidationError('No rooms available')

        room = available_rooms.first()
        room.patient = patient
        room.doctor = doctor
        room.expires_at = timezone.now() + timezone.timedelta(days=days)
        room.save()
        return room

    def create_room(self,number):
        if self.filter(number=number).exists():
            raise ValidationError('Room number already exists')
        return self.create(number=number)

    def clear_expired_rooms(self):
        expired_rooms = self.filter(expires_at__lt=timezone.now())
        for room in expired_rooms:
            room.patient = None
            room.doctor = None
            room.save()


class Room(BaseModel):
    number = models.PositiveSmallIntegerField(unique=True)
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, null=True, blank=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, blank=True,related_name='rooms')
    expires_at = models.DateTimeField(null=True, blank=True)

    objects = RoomManager()

    def __str__(self):
        return f"Room {self.number}"
