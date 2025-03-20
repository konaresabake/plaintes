from django import forms
from .models import *

class ReportForm(forms.ModelForm):
    class Meta:
        model = Plainte
        fields = ['title', 'description', 'category', 'status', 'location']
