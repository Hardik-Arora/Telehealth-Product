# Generated by Django 3.2.3 on 2021-06-02 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0003_rename_employement_patientprofile_employment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patientprofile',
            old_name='DOB',
            new_name='dob',
        ),
        migrations.RemoveField(
            model_name='patientprofile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='patientprofile',
            name='last_name',
        ),
    ]
