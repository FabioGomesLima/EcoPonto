from django.shortcuts import render, redirect
from .models import PontosDeColeta 
from .forms import PontoForm

# Create your views here.


def index (request):
    return render(request, 'index.html')

def PontosDeColeta(request):
    pontos = Ponto.objects.all()
    contexto = {
        'pontos': pontos
    }
    return render(request,'Pontos.html', contexto)

def cadastro_ponto(request):
    form = PontoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('PontosDeColeta')
    contexto = {
        'form': form
    }
    return render(request,'Cadastro_ponto.html', contexto)

def editar_ponto(request, id):
    ponto = PontosDeColeta.objects.get(pk=id)
    form = PontoForm(request.POST or None, instance=ponto)
    if form.is_valid():
        form.save()
        return redirect('PontosDeColeta')
    contexto = {
        'form': form
    }
    return render(request, 'Cadastro_ponto.html', contexto)


def remover_ponto(request, id):
    ponto =  Ponto.objects.get(pk=id)
    ponto.delete()
    return redirect('PontosDeColeta')