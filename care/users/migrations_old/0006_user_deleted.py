# Generated by Django 2.2.11 on 2020-03-21 18:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0005_auto_20200321_0601"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="deleted",
            field=models.BooleanField(default=False),
        ),
    ]