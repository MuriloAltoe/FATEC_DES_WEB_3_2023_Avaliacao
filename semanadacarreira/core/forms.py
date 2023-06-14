from django import forms
from .models import Pessoa

class formProf(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ('nome', 'professor')
