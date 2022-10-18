# Generated by Django 4.1.2 on 2022-10-18 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=100)),
                ('chief_complaint', models.TextField(max_length=500)),
                ('current_condition', models.TextField(max_length=500)),
                ('past_medical_history', models.TextField(max_length=500)),
            ],
        ),
    ]