from django.forms import ModelForm
from django import forms
from .models import TemaForo

class TemaForoForm(forms.ModelForm):
    class Meta:
        model = TemaForo
        fields = ['titulo', 'mensaje']
        widgets = {
            'fecha_creacion': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
