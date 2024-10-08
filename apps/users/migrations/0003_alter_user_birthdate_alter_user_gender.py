# Generated by Django 5.1 on 2024-08-20 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_user_address_user_avatar_user_birthdate_user_gender_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="birthdate",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="user",
            name="gender",
            field=models.CharField(
                choices=[("man", "Man"), ("woman", "Woman")], max_length=5
            ),
        ),
    ]
