from django.forms import ModelForm
from .models import PontosDeColeta, Usuarios 


class PontoDeColetaForm(ModelForm):
    class Meta:
        model = PontosDeColeta
        fields = ['tipo', 'descricao', 'imagem', 'usuario']


class UsuariosForm(ModelForm):
    class Meta:
        model = Usuarios
        fields = ['email']