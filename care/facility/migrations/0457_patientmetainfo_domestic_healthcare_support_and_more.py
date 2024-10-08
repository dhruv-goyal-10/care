# Generated by Django 4.2.10 on 2024-09-19 07:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0456_dailyround_appetite_dailyround_bladder_drainage_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="patientmetainfo",
            name="domestic_healthcare_support",
            field=models.SmallIntegerField(
                blank=True,
                choices=[
                    (0, "NO_SUPPORT"),
                    (10, "FAMILY_MEMBER"),
                    (20, "PAID_CAREGIVER"),
                ],
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="patientmetainfo",
            name="socioeconomic_status",
            field=models.SmallIntegerField(
                blank=True,
                choices=[
                    (10, "VERY_POOR"),
                    (20, "POOR"),
                    (30, "MIDDLE_CLASS"),
                    (40, "WELL_OFF"),
                ],
                null=True,
            ),
        ),
    ]
