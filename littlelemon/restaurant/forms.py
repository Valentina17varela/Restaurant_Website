from django import forms
from .models import Recomendation


class RecomendationForm(forms.ModelForm):
    class Meta:
        model = Recomendation
        fields = ["name", "email", "message"]
