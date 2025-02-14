from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import index, PontosDeColeta, cadastro_ponto, editar_ponto, remover_ponto

urlpatterns = [
    path('', index, name= 'index' ),
    path('PontosDeColeta/', PontosDeColeta, name='PontosDeColeta'),
    path('cadastro_ponto/', cadastro_ponto, name='cadastro_ponto'),
    path('editar_ponto/<int:id>/', editar_ponto, name='editar_ponto'),
    path('remover_ponto/<int:id>', remover_ponto, name='remover_ponto'),
    
]
