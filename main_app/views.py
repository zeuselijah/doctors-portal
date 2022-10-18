from django.shortcuts import render
from . models import Patient


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def patients_index(request):
    patients = Patient.objects.all()
    return render(request, 'patients/index.html', {'patients': patients})


