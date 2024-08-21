from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import OneToOneField, ForeignKey, PositiveSmallIntegerField, CharField, CASCADE, TextField, \
    DecimalField

from apps.hospital.models import Department
from apps.shared.models import BaseModel
from apps.users.models import User


class Specialities(BaseModel):
    name = CharField(max_length=256)
    description = TextField(blank=True, default=name)
    cost = DecimalField(max_digits=10,decimal_places=2,validators=[MinValueValidator(0)], default=50)


class Doctor(BaseModel):
    user = OneToOneField(User, on_delete=CASCADE, related_name='doctor')
    department = ForeignKey(Department, on_delete=CASCADE, related_name='doctors')
    experience = PositiveSmallIntegerField(default=0)
    speciality = ForeignKey(Specialities, on_delete=CASCADE, related_name='doctors')
