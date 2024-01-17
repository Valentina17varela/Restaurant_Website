from django import forms
from .models import Recomendation, Book
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget
from .models import Book


class RecomendationForm(forms.ModelForm):
    class Meta:
        model = Recomendation
        fields = ["name", "email", "message"]
