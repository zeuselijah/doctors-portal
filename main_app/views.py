from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def patients_index(request):
    return render(request, 'patients/index.html', {'patients': patients})

class Patient:
    def __init__(self, name, age, gender, chief_complaint, current_condition, past_medical_history):
        self.name = name
        self.age = age
        self.gender = gender
        self.chief_complaint = chief_complaint
        self.current_condition = current_condition
        self.past_medical_history = past_medical_history

patients = [
    Patient('Test One', 21, 'Male', 'Difficulty in Breathing', 'Labored Breathing', 'Asthma'),
    Patient('Test Two', 22, 'Female', 'Chest Pain', 'Heart beating fast', 'Heart Failure'),
    Patient('Test Three', 23, 'Male', 'Injury from fall', 'Head pain and bleeding from the head', 'None'),
] 
