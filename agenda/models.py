from django.db import models


class Servico(models.Model):
    nome = models.CharField(max_length=100)
    duracao = models.PositiveIntegerField()  # Duração em minutos
    preco = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.nome

class Agendamento(models.Model):
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    cliente_nome = models.CharField(max_length=100)
    cliente_email = models.EmailField()

    def __str__(self):
        return f'Agendamento de {self.cliente_nome} para {self.servico.nome} em {self.data_hora}'
# Create your models here.
