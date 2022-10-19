from django.forms import ModelForm
from .models import Prescriptions_Given

class PrescriptionsGivenForm(ModelForm):
    class Meta:
        model = Prescriptions_Given
        fields = ('date', 'time', 'prescriptionsGiven')