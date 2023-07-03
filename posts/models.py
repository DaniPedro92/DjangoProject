from django.db import models

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length = 200)
    imagem = models.ImageField(upload_to='images/')

    def __str__(self) -> str:
        return self.titulo