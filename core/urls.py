from django.urls import path
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static

from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('pontos/', views.Listar_pontos, name='Listar_pontos'),
    path('ponto_cadastrar', views.cadastrar_pontos, name='ponto_cadastrar'),
    path('login/', LoginView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('ponto_excluir/<int:ponto_id>/', views.excluir_ponto, name='ponto_excluir'),
    path('ponto_editar/<int:ponto_id>/', views.editar_ponto, name='editar_ponto')
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
