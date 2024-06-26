# Generated by Django 4.2.8 on 2024-01-31 17:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0407_alter_dailyround_additional_symptoms_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalpatientregistration",
            name="date_of_delivery",
            field=models.DateField(
                default=None, null=True, verbose_name="Date of Delivery"
            ),
        ),
        migrations.AddField(
            model_name="historicalpatientregistration",
            name="last_menstruation_start_date",
            field=models.DateField(
                default=None, null=True, verbose_name="Last Menstruation Start Date"
            ),
        ),
        migrations.AddField(
            model_name="patientregistration",
            name="date_of_delivery",
            field=models.DateField(
                default=None, null=True, verbose_name="Date of Delivery"
            ),
        ),
        migrations.AddField(
            model_name="patientregistration",
            name="last_menstruation_start_date",
            field=models.DateField(
                default=None, null=True, verbose_name="Last Menstruation Start Date"
            ),
        ),
    ]
