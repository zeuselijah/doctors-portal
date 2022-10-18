from django.db import models

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    chief_complaint = models.TextField(max_length=500)
    current_condition = models.TextField(max_length=500)
    past_medical_history = models.TextField(max_length=500)

def __str__(self):
    return self.name