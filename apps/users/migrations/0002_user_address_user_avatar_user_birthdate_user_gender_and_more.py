# Generated by Django 5.1 on 2024-08-20 16:02

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="address",
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="avatar",
            field=models.ImageField(
                default="avatars/default.jpg", upload_to="avatars/"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="birthdate",
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name="user",
            name="gender",
            field=models.CharField(
                choices=[("man", "Man"), ("woman", "Woman")],
                default="man",
                max_length=5,
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="phone_number",
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True, max_length=128, null=True, region=None
            ),
        ),
    ]
