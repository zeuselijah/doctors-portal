from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Patient, Prescription
from .forms import PrescriptionsGivenForm


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def patients_index(request):
    patients = Patient.objects.all()
    return render(request, 'patients/index.html', {'patients': patients})

def patients_detail(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    prescriptionsGiven_form = PrescriptionsGivenForm()
    prescriptions = Prescription.objects.exclude(id__in = patient.prescriptions.all().values_list('id'))
    return render(request, 'patients/detail.html', 
    { 
        'patient': patient,
        'prescriptionsGiven_form': prescriptionsGiven_form, 
        'prescriptions': prescriptions 
    })

def add_prescriptionsGiven(request, patient_id):
    form = PrescriptionsGivenForm(request.POST)
    if form.is_valid():
        new_prescriptionsGiven = form.save(commit=False)
        new_prescriptionsGiven.patient_id = patient_id
        new_prescriptionsGiven.save()
    else:
        print(form.errors)
        return redirect('patients_detail', patient_id=patient_id)

def assoc_prescription(request, patient_id, prescription_id):
    Patient.objects.get(id=patient_id).prescriptions.add(prescription_id)
    return redirect('patients_detail', patient_id=patient_id)

class PatientsCreate(CreateView):
    template_name= 'patients/patient_form.html'
    model = Patient
    fields = ['name', 'age', 'gender', 'chief_complaint', 'current_condition', 'past_medical_history']
    success_url = '/patients/'

class PatientsUpdate(UpdateView):
    model = Patient
    fields = ['chief_complaint', 'current_condition', 'past_medical_history']
    success_url = '/patients/'

class PatientsDelete(DeleteView):
    model = Patient
    success_url = '/patients/'

class PrescriptionsCreate(CreateView):
    template_name = 'prescriptions/prescription_form.html'
    model = Prescription
    fields = ('name', 'dosage')
    
    

class PrescriptionsIndex(ListView):
    template_name = 'prescriptions/index.html'
    model = Prescription 

class PrescriptionsDetail(DetailView):
    template_name = 'prescriptions/detail.html'
    model = Prescription 
    

class PrescriptionsUpdate(UpdateView):
    template_name = 'prescriptions/prescription_form.html'
    model = Prescription
    fields = ('name','dosage')
    

class PrescriptionsDelete(DeleteView):
    model = Prescription
    success_url = '/prescriptions/'

