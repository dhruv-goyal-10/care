# Generated by Django 4.2.2 on 2023-12-02 04:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("abdm", "0011_alter_abhanumber_abha_number_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="consentrequest",
            name="status",
            field=models.CharField(
                choices=[
                    ("REQUESTED", "Requested"),
                    ("GRANTED", "Granted"),
                    ("DENIED", "Denied"),
                    ("EXPIRED", "Expired"),
                    ("REVOKED", "Revoked"),
                ],
                default="REQUESTED",
                max_length=20,
            ),
        ),
    ]