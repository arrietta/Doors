# doors/forms.py

from django import forms
from .models import Door

class DoorForm(forms.ModelForm):
    class Meta:
        model = Door
        fields = ['shape', 'color', 'molding', 'portal']
