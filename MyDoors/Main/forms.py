from django import forms
from .models import Basket


class DoorForm(forms.ModelForm):
    class Meta:
        model = Basket
        fields = ['code', 'door']
