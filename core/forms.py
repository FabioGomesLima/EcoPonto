from django import forms
from .models import PontosDeColeta


class PontoForm(forms.ModelForm):
    class Meta:
        model = PontosDeColeta
        fields = ['descricao', 'imagem', 'tipo', 'usuario']
        widgets = {
            'tipo': forms.RadioSelect(),
            'usuario': forms.CheckboxSelectMultiple(),
        }