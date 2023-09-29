# forms.py

from django import forms
from .models import Shape, Molding, Portal, Color

class DoorFilterForm(forms.Form):
    shape = forms.ModelChoiceField(queryset=Shape.objects.all(), empty_label="Select Shape")
    molding = forms.ModelChoiceField(queryset=Molding.objects.all(), empty_label="Select Molding", required=False)
    portal = forms.ModelChoiceField(queryset=Portal.objects.all(), empty_label="Select Portal", required=False)
    color = forms.ModelChoiceField(queryset=Color.objects.all(), empty_label="Select Color")
