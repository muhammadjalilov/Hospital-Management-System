from django.contrib import admin
from apps.hospital.models import Hospital, Department, Staff

admin.site.register(Hospital)
admin.site.register(Department)
admin.site.register(Staff)
