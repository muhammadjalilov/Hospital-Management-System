# Generated by Django 5.1 on 2024-08-22 08:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("appointments", "0010_prescription_doctor"),
        ("doctor", "0006_remove_specialities_department_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="prescription",
            name="doctor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="prescriptions",
                to="doctor.doctor",
            ),
        ),
    ]
