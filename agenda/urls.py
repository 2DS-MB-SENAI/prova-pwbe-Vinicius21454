# agenda/urls.py
from django.urls import path
from .views import servicos_list, servico_detail, agendamentos_list, agendamento_detail

urlpatterns = [
    path('servicos/', servicos_list, name='servicos_list'),
    path('servicos/<int:id>/', servico_detail, name='servico_detail'),
    path('agendamentos/', agendamentos_list, name='agendamentos_list'),
    path('agendamentos/<int:id>/', agendamento_detail, name='agendamento_detail'),
]