# Generated by Django 5.1 on 2024-08-21 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("doctor", "0003_remove_specialities_department_and_more"),
        ("hospital", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="specialities",
            name="department",
            field=models.ManyToManyField(
                related_name="specialities", to="hospital.department"
            ),
        ),
    ]
