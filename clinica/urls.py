from django.urls import path
from .views import listar_medicos, criar_consulta, detalhes_consulta

urlpatterns = [
    path('medicos/', listar_medicos, name='listar_medicos'),
    path('consultas/nova/', criar_consulta, name='criar_consulta'),
    path('consultas/<int:id>/', detalhes_consulta, name='detalhes_consulta'),
]