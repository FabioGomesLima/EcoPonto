from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import PontosDeColeta
from .forms import PontoDeColetaForm



def index(request):
  return render(request, 'index.html')  
    
    
    
def Listar_pontos(request):
    pontos = PontosDeColeta.objects.all()
    contexto = { 
         'todos_pontos':pontos     
    }
    return render(request, 'Pontos.html',contexto )
  
@login_required 
def cadastrar_pontos(request):
  if request.method == 'POST':
    form = PontoDeColetaForm(request.POST , request.FILES)
  
    if form.is_valid():
      form.save()
      return redirect('Listar_pontos')
  else:
    form = PontoDeColetaForm()
  contexto = { 
         'form_ponto': form   
    }
  return render(request, 'Cadastro_pontos.html',  contexto)
  
def is_admin(user):
    return user.is_superuser

@login_required
@user_passes_test(is_admin)  # Apenas administradores podem excluir
def excluir_ponto(request, ponto_id):
    ponto = get_object_or_404(PontosDeColeta, id=ponto_id)
    ponto.delete()
    return redirect('Listar_pontos')