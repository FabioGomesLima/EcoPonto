from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import PontosDeColeta
from .forms import PontoDeColetaForm, UsuariosForm
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth import logout

def is_admin(user):
    return user.is_superuser

def index(request):
    return render(request, 'index.html') 

def cadastro_coletor(request):
    form = UsuariosForm(request.POST)
    if form.is_valid():
        usuario = form.save(commit=False)
        usuario.is_superuser = True
        usuario.save()
        return redirect('login')

    contexto={
        "form":form
    }
    return render(request, 'registration/cadastrar_coletor.html', contexto)

def cadastrar_user(request):
    form = UsuariosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    contexto ={
        'form': form
    }
    return render(request, 'registration/cadastrar_user.html', contexto)
    

def Listar_pontos(request):
    pontos = PontosDeColeta.objects.all()
    contexto = { 
         'todos_pontos':pontos     
    }
    return render(request, 'Pontos.html',contexto )
  
@login_required
@user_passes_test(is_admin)
def Listar_pontos_admin(request):
    user = request.user
    pontos = PontosDeColeta.objects.filter(usuario=user)
    
    contexto = { 
         'todos_pontos': pontos     
    }
    
    return render(request, 'Pontos.html', contexto)

@login_required
@user_passes_test(is_admin)
def cadastrar_pontos(request):
    if request.method == 'POST':
        form = PontoDeColetaForm(request.POST, request.FILES)
        if form.is_valid():
            ponto = form.save(commit=False)
            ponto.usuario = request.user
            ponto.save()  
            return redirect('Listar_pontos')
    else:
        form = PontoDeColetaForm()
    
    contexto = {'form_ponto': form}
    return render(request, 'Cadastro_pontos.html', contexto)


@login_required
@user_passes_test(is_admin)  # Apenas administradores podem excluir
def excluir_ponto(request, ponto_id):
    ponto = get_object_or_404(PontosDeColeta, id=ponto_id)
    ponto.delete()
    return redirect('Listar_pontos')

@login_required
@user_passes_test(is_admin)
def editar_ponto(request, ponto_id):
  ponto = get_object_or_404(PontosDeColeta, pk=ponto_id)
    
  if request.method == 'POST':
    form = PontoDeColetaForm(request.POST, request.FILES, instance=ponto)
    if form.is_valid():
        form.save()
        return redirect('Listar_pontos')
  else:
    form = PontoDeColetaForm(instance=ponto)
  
  contexto = {'form_ponto': form}
  return render(request, 'Cadastro_pontos.html', contexto)

def listar_pontos_coleta(request):
    pontos = PontosDeColeta.objects.all()
    data = [{"nome": p.nome, "latitude": p.latitude, "longitude": p.longitude, "tipo_residuo": p.tipo_residuo} for p in pontos]
    return JsonResponse(data, safe=False)

def mapa_pontos_coleta(request):
    return render(request, 'mapa.html')


def custom_logout(request):
    logout(request)
    return redirect('index')