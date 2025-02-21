from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PontoDeColetaSerializer
from .models import PontosDeColeta

@api_view(['GET'])
def pontosAPIlistar(request):
    pontos = PontosDeColeta.objects.all()
    pontos_serializer = PontoDeColetaSerializer(pontos, many=True)
    return Response(pontos_serializer.data)

@api_view(['PUT'])
def pontoAPIadicionar(request):
    pontos = PontoDeColetaSerializer(data=request.data)
    if pontos.is_valid():
        pontos.save()
        return Response(pontos.data, status=status.HTTP_201_CREATED)
    
@api_view(['POST'])
def pontoAPIatualizar(request,id):
    ponto_bd = PontosDeColeta.objects.get(id=id)
    ponto = PontoDeColetaSerializer(data=request.data, instance=ponto_bd)
    if ponto.is_valid():
        ponto.save()
        return Response(ponto.data, status=status.HTTP_202_ACCEPTED)
    
@api_view(['DELETE'])
def pontoAPIremover(request,id):
    ponto_bd = PontosDeColeta.objects.get(id=id)
    if ponto_bd:
        ponto_bd.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    