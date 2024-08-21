from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import OneToOneField, ForeignKey, PositiveSmallIntegerField, CharField, CASCADE, TextField, \
    DecimalField, ManyToManyField, BooleanField

from apps.hospital.models import Department
from apps.shared.models import BaseModel
from apps.users.models import User


class Specialities(BaseModel):
    name = CharField(max_length=256)
    description = TextField(blank=True, default=name)
    department = ManyToManyField(Department,related_name='specialities')
    cost = DecimalField(max_digits=10,decimal_places=2,validators=[MinValueValidator(0)], default=50)

    def __str__(self):
        return self.name


class Doctor(BaseModel):
    user = OneToOneField(User, on_delete=CASCADE, related_name='doctor')
    experience = PositiveSmallIntegerField(default=0)
    speciality = ForeignKey(Specialities, on_delete=CASCADE, related_name='doctors')
    status = BooleanField(default=False)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
