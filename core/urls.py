from django.urls import path
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from .views import listar_pontos_coleta, mapa_pontos_coleta
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrar_user/', views.cadastrar_user, name='cadastrar_user'),
    path('cadastrar_coletor/', views.cadastro_coletor, name='cadastrar_coletor'),
    path('pontos/', views.Listar_pontos, name='Listar_pontos'),
    path('ponto_cadastrar', views.cadastrar_pontos, name='ponto_cadastrar'),
    path('login/', LoginView.as_view(), name='login'),
    path("logout/",views.custom_logout, name="logout"),
    path('ponto_excluir/<int:ponto_id>/', views.excluir_ponto, name='ponto_excluir'),
    path('ponto_editar/<int:ponto_id>/', views.editar_ponto, name='editar_ponto'),
    path('pontos-coleta/', listar_pontos_coleta, name='listar_pontos_coleta'),
    path('pontos-coleta-admin/', views.Listar_pontos_admin, name='listar_pontos_coleta_admin'),
    path('mapa/', mapa_pontos_coleta, name='mapa_pontos_coleta')
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
