from django import forms
from .models import FlightItinerary

class MyForm(forms.ModelForm):
    class Meta:
        model = FlightItinerary
        fields = "__all__"