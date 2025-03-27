from django.db import models

class Cotacao(models.Model):
    data = models.DateField()
    moeda = models.CharField(max_length=3)  # BRL, EUR, JPY
    valor = models.DecimalField(max_digits=10, decimal_places=4)

    def __str__(self):
        return f"{self.moeda} - {self.data}: {self.valor}"
