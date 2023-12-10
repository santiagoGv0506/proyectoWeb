from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class TemaForo(models.Model):
    titulo = models.CharField(max_length=255)
    mensaje = models.TextField(default='')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo + '-by ' + self.autor.username