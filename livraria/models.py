from datetime import datetime
from django.db import models

# Create your models here.

class Editora(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.nome

    class Meta:
        ordering = ['nome']

class Livro(models.Model):
    TIPOS = (
        ('Paperback', 'Paperback'),
        ('Hardcover', 'Hardcover')
    )

    titulo = models.CharField(max_length=200)
    ano = models.SmallIntegerField(blank=True, null=True, default=datetime.now().year)
    isbn = models.CharField(max_length=20, blank=True, null = True)
    imagem = models.ImageField(upload_to='livros/',blank=True, null = True)
    descricao = models.TextField(blank=True, null=True)
    tipo = models.CharField(max_length=20, blank=True, null = True, choices = TIPOS, default='Paperback')
    editora = models.ForeignKey(Editora, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self) -> str:
        return F"{self.titulo}, de {self.ano}, {self.editora}"
    
    class Meta:
        ordering = ["titulo"]