from django.contrib import admin
from .models import Patient, Prescriptions_Given, Prescription

# Register your models here.
admin.site.register(Patient)
admin.site.register(Prescriptions_Given)
admin.site.register(Prescription)
