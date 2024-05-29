from django.db import models
from registro.models import Pessoa
from listaferramentas.models import Ferramenta

class Reserva(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    ferramenta = models.ForeignKey(Ferramenta, on_delete=models.CASCADE)
    data_reserva = models.DateField()

    def __str__(self):
        return f"Reserva de {self.ferramenta} por {self.pessoa} em {self.data_reserva}"
