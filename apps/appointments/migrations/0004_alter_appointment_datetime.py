# Generated by Django 5.1 on 2024-08-21 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("appointments", "0003_prescription_pharmacy"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appointment",
            name="datetime",
            field=models.DateTimeField(),
        ),
    ]
