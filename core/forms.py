from django import forms
from .models import PontosDeColeta, Usuarios
from django.contrib.auth.forms import UserCreationForm


class PontoDeColetaForm(forms.ModelForm):
    class Meta:
        model = PontosDeColeta
        fields = ['tipo', 'descricao', 'imagem']


class UsuariosForm(UserCreationForm):
    class Meta:
        model = Usuarios
        fields = ['username','email','password1', 'password2']
        labels = {
            'username': 'Nome de Usuário',
            'email': 'Endereço de E-mail',
            'password1': 'Senha',
            'password2': 'Confirmar Senha',
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite seu nome de usuário',
                'style': 'width: 80%; padding: 10px; margin-bottom: 10px;'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite seu e-mail',
                'style': 'width: 80%; padding: 10px; margin-bottom: 10px;'
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha',
                'style': 'width: 100%; padding: 10px; margin-bottom: 10px;'
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Confirme sua senha',
                'style': 'width: 100%; padding: 10px; margin-bottom: 20px;'
            }),
        }