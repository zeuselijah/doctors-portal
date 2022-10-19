from random import choices
from django.db import models
from django.urls import reverse

# Create your models here.
class Prescription(models.Model):
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} {self.dosage}'
    
    def get_absolute_url(self):
        return reverse('prescriptions_detail', kwargs={'pk': self.id})

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    chief_complaint = models.CharField(max_length=500)
    current_condition = models.TextField(max_length=500)
    past_medical_history = models.TextField(max_length=500)
    prescriptions = models.ManyToManyField(Prescription)

def __str__(self):
    return self.name

def get_absolute_url(self):
    return reverse('patients_detail', kwargs={'patient_id': self.id})

class Prescriptions_Given(models.Model):
    PRESCRIPTIONS_GIVEN = (
        ('P', 'Pain Medication'),
        ('A', 'Anitbiotics'),
        ('F', 'Fluids'),
    )

    class Meta:
        ordering = ('-date', '-time')

    date = models.DateField('Prescription Date')
    time = models.TimeField(auto_now=False, auto_now_add=False)
    prescription_given = models.CharField(max_length=1, choices=PRESCRIPTIONS_GIVEN, default=PRESCRIPTIONS_GIVEN[0][0])
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_prescription_given_display()} on {self.date} at {self.time}'