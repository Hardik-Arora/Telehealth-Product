# Generated by Django 3.2.3 on 2021-06-27 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appointment', '0004_remove_appointment_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='start_time',
            field=models.TimeField(),
        ),
    ]