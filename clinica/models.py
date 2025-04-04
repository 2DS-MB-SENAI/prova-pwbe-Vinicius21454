# clinica/models.py
from django.db import models
from django.core.exceptions import ValidationError
import re
from django.utils import timezone

class Medico(models.Model):
    ESPECIALIDADES = [
        ('cardiologia', 'Cardiologia'),
        ('dermatologia', 'Dermatologia'),
        ('pediatria', 'Pediatria'),
        ('ortopedia', 'Ortopedia'),
        # Adicione mais especialidades conforme necessário
    ]

    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=50, choices=ESPECIALIDADES)
    crm = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True, null=True)

    def clean(self):
        # Validação do CRM
        if not re.match(r'^\d{2}/\d{5}$', self.crm):
            raise ValidationError('O CRM deve ter o formato XX/XXXXX.')
        # Validação do nome
        if len(self.nome) < 5:
            raise ValidationError('O nome deve ter pelo menos 5 caracteres.')

    def __str__(self):
        return self.nome

class Consulta(models.Model):
    STATUS_CHOICES = [
        ('agendado', 'Agendado'),
        ('realizado', 'Realizado'),
        ('cancelado', 'Cancelado'),
    ]

    paciente = models.CharField(max_length=100)
    data = models.DateTimeField()
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def clean(self):
        # Validação da data
        if self.data < timezone.now():
            raise ValidationError('Não é permitido agendar consultas no passado.')

    def __str__(self):
        return f'Consulta de {self.paciente} com {self.medico.nome} em {self.data}'


