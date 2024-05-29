from django.db import models

class Pessoa(models.Model):
    CARGO_CHOICES = (
        ('electricista', 'Electricista'),
        ('serralheiro', 'Serralheiro'),
        ('ajudante', 'Ajudante'),
        ('instrumentista', 'Instrumentista'),
        ('outro', 'Outro'),
    )

    nome = models.CharField(max_length=100, default="")
    email = models.EmailField()
    data_nascimento = models.DateField(null=True)
    cargo = models.CharField(max_length=100, choices=CARGO_CHOICES)

    def __str__(self):
        return self.nome
