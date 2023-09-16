from django import forms
from .models import Doors

class DoorsForm(forms.ModelForm):
    class Meta:
        model = Doors
        fields = ['shape', 'color', 'molding', 'portal']

    shape = forms.ChoiceField(choices=Doors.SHAPE_CHOICES)
    color = forms.ChoiceField(choices=Doors.COLOR_CHOICES)
    molding = forms.ChoiceField(choices=Doors.MOLDING_CHOICES)
    portal = forms.ChoiceField(choices=Doors.PORTAL_CHOICES)
