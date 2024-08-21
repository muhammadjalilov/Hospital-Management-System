from django.db.models import OneToOneField, CASCADE, ForeignKey, Sum, DecimalField

from apps.hospital.models import Staff
from apps.shared.models import BaseModel
from apps.users.models import User


class Patient(BaseModel):
    user = OneToOneField(User, on_delete=CASCADE, related_name='patient')

    total_cost = DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def get_total_cost_invoices(self):
        return self.invoices.aggregate(total=Sum('cost'))['total'] or 0

    def save(self, *args, **kwargs):
        self.total_cost = self.get_total_cost_invoices()
        super().save(*args, **kwargs)


class Room(BaseModel):
    patient = OneToOneField(Patient, on_delete=CASCADE)
    staff = ForeignKey(Staff, on_delete=CASCADE, related_name='rooms')
