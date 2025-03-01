from django.forms import ModelForm
from .models import PontosDeColeta, Usuarios
from django.contrib.auth.forms import UserCreationForm


class PontoDeColetaForm(ModelForm):
    class Meta:
        model = PontosDeColeta
        fields = ['tipo', 'descricao', 'imagem']


class UsuariosForm(UserCreationForm):
    class Meta:
        model = Usuarios
        fields = ['username','email','password1', 'password2']