# Generated by Django 4.1.2 on 2022-10-19 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_prescriptions_given'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prescriptions_given',
            old_name='prescription_given',
            new_name='prescriptionsGiven',
        ),
    ]
