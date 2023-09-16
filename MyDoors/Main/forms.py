from django import forms
from .models import Doors

class DoorsForm(forms.ModelForm):
    class Meta:
        model = Doors
        fields = ['shape', 'color', 'molding', 'portal']
