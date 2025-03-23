from django import forms
from .models import Mountain, Climber, Climb

class MountainForm(forms.ModelForm):
    class Meta:
        model = Mountain
        fields = ['name', 'height', 'country', 'region']

class ClimberForm(forms.ModelForm):
    class Meta:
        model = Climber
        fields = ['name', 'address']

class ClimbForm(forms.ModelForm):
    class Meta:
        model = Climb
        fields = ['start_date', 'end_date', 'mountain', 'climbers']
