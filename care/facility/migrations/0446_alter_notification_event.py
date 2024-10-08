# Generated by Django 4.2.10 on 2024-07-18 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("facility", "0445_merge_20240715_0301"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notification",
            name="event",
            field=models.IntegerField(
                choices=[
                    (0, "MESSAGE"),
                    (20, "PATIENT_CREATED"),
                    (30, "PATIENT_UPDATED"),
                    (40, "PATIENT_DELETED"),
                    (50, "PATIENT_CONSULTATION_CREATED"),
                    (60, "PATIENT_CONSULTATION_UPDATED"),
                    (70, "PATIENT_CONSULTATION_DELETED"),
                    (80, "INVESTIGATION_SESSION_CREATED"),
                    (90, "INVESTIGATION_UPDATED"),
                    (100, "PATIENT_FILE_UPLOAD_CREATED"),
                    (110, "CONSULTATION_FILE_UPLOAD_CREATED"),
                    (120, "PATIENT_CONSULTATION_UPDATE_CREATED"),
                    (130, "PATIENT_CONSULTATION_UPDATE_UPDATED"),
                    (140, "PATIENT_CONSULTATION_ASSIGNMENT"),
                    (200, "SHIFTING_UPDATED"),
                    (210, "PATIENT_NOTE_ADDED"),
                    (220, "PUSH_MESSAGE"),
                    (230, "PATIENT_PRESCRIPTION_CREATED"),
                    (240, "PATIENT_PRESCRIPTION_UPDATED"),
                ],
                default=0,
            ),
        ),
    ]
