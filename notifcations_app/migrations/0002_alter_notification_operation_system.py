# Generated by Django 3.2.9 on 2022-04-14 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notifcations_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notification",
            name="operation_system",
            field=models.CharField(
                choices=[
                    ("ANY", "Any os"),
                    ("MACOS", "Apple MacOS"),
                    ("LINUX", "Linux"),
                    ("WINDOWS", "Microsoft Windows"),
                ],
                default="ANY",
                max_length=24,
            ),
        ),
    ]