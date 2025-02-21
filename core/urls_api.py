from django.urls import path
from .views_api import pontosAPIlistar, pontoAPIadicionar,pontoAPIatualizar,pontoAPIremover


urlpatterns = [
    path('pontos/listar/',pontosAPIlistar ),
    path('ponto/adicionar/', pontoAPIadicionar),
    path('ponto/atualizar/<int:id>/',pontoAPIatualizar ),
    path('ponto/remover/<int:id>/', pontoAPIremover ),
]