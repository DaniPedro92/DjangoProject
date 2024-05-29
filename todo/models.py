from django.db import models

# Create your models here.
class Tarefa(models.Model):
    titulo = models.CharField(max_length=200)
    realizado = models.BooleanField(default=False)
    data = models.DateTimeField(auto_now_add=True)  

    def __str__(self) -> str:
        return self.titulo