# Generated by Django 3.2.3 on 2021-05-29 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='years_of_experience',
            field=models.IntegerField(null=True),
        ),
    ]