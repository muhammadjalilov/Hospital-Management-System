from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    created_at = models.DateField(auto_now_add=timezone.now())
    updated_at = models.DateTimeField(auto_now=timezone.now())

    class Meta:
        abstract = True
