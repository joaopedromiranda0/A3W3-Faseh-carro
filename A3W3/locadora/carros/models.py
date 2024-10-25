from django.db import models
from django.contrib.auth.models import User

class Carro(models.Model):
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    ano = models.IntegerField()
    preco_diaria = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.ano})"

class Reserva(models.Model):
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data_reserva = models.DateField()
    data_devolucao = models.DateField()

    def __str__(self):
        return f"Reserva de {self.carro} por {self.usuario}"
