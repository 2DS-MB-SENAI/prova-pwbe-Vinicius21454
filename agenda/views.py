# agenda/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Servico, Agendamento
from .serializers import ServicoSerializer, AgendamentoSerializer

# Endpoints para Serviços
@api_view(['GET', 'POST'])
def servicos_list(request):
    if request.method == 'GET':
        servicos = Servico.objects.all()
        serializer = ServicoSerializer(servicos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ServicoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def servico_detail(request, id):
    try:
        servico = Servico.objects.get(id=id)
    except Servico.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ServicoSerializer(servico)
    return Response(serializer.data)

# Endpoints para Agendamentos
@api_view(['GET', 'POST'])
def agendamentos_list(request):
    if request.method == 'GET':
        agendamentos = Agendamento.objects.all()
        serializer = AgendamentoSerializer(agendamentos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AgendamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def agendamento_detail(request, id):
    try:
        agendamento = Agendamento.objects.get(id=id)
    except Agendamento.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = AgendamentoSerializer(agendamento)
    return Response(serializer.data)