from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, redirect

from .models import Patient, Prescription

from django.contrib.auth import login


from .forms import PrescriptionsGivenForm
from django.contrib.auth.forms import UserCreationForm 


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def patients_index(request):
    patients = Patient.objects.filter(user=request.user)
    return render(request, 'patients/index.html', {'patients': patients})

@login_required
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

@login_required
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

def remove_prescription(request, patient_id, prescription_id):
    Patient.objects.get(id=patient_id).prescriptions.remove(prescription_id)
    return redirect('patients_detail', patient_id=patient_id)

def signup(request):
    error_message = None
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('patients_index')
        else:
            error_message = 'Signup input invalid - Please try again'
    form = UserCreationForm()
    context = { 'form': form, 'error': error_message }
    return render(request, 'registration/signup.html', context)

class PatientsCreate(LoginRequiredMixin, CreateView):
    template_name= 'patients/patient_form.html'
    model = Patient
    fields = ['name', 'age', 'gender', 'chief_complaint', 'current_condition', 'past_medical_history']
    success_url = '/patients/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PatientsUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'patients/patient_form.html'
    model = Patient
    fields = ['chief_complaint', 'current_condition', 'past_medical_history']
    success_url = '/patients/'

class PatientsDelete(LoginRequiredMixin, DeleteView):
    model = Patient
    success_url = '/patients/'

class PrescriptionsCreate(LoginRequiredMixin, CreateView):
    template_name = 'prescriptions/prescription_form.html'
    model = Prescription
    fields = ('name', 'dosage')
    
class PrescriptionsIndex(LoginRequiredMixin, ListView):
    template_name = 'prescriptions/index.html'
    model = Prescription 

class PrescriptionsDetail(LoginRequiredMixin, DetailView):
    template_name = 'prescriptions/detail.html'
    model = Prescription 
    
class PrescriptionsUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'prescriptions/prescription_form.html'
    model = Prescription
    fields = ('name','dosage')
    
class PrescriptionsDelete(LoginRequiredMixin, DeleteView):
    model = Prescription
    success_url = '/prescriptions/'

