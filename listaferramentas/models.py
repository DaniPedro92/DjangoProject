from datetime import datetime
from django.db import models

class ListaFerramenta(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.nome
    
    class Meta:
        ordering = ['nome']


class Ferramenta(models.Model):
    titulo = models.CharField(max_length=200)
    ano = models.SmallIntegerField(blank=True, null=True, default=datetime.now().year)
    imagem = models.ImageField(upload_to='livros/', blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    tipo = models.CharField(max_length=200, blank=True, null=True)
    stock = models.PositiveIntegerField(default=0) 

    def __str__(self) -> str:
        return self.titulo + ", " + str(self.ano)
    
    class Meta:
        ordering = ['titulo']