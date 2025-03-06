from rest_framework import serializers
from .models import PontosDeColeta, Usuarios

class PontoDeColetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PontosDeColeta
        fields = ['tipo', 'descricao', 'imagem', 'usuario']

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = ['username','email','password1', 'password2']