# Generated by Django 5.1.1 on 2025-01-20 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0009_subject_data_bl13_subject_data_bl14_subject_data_m13_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subject_data",
            name="m13",
            field=models.IntegerField(default=0),
        ),
    ]
