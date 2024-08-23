# Generated by Django 5.1 on 2024-08-21 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_alter_user_birthdate_alter_user_gender"),
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
