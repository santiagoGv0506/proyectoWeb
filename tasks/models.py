from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Notas(models.Model):
    title= models.CharField(max_length=150)
    created= models.DateTimeField(auto_now_add=True)
    datecompleted= models.DateTimeField(null = True)
    nota=models.FloatField(default=0.0)
    user= models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + '-by ' +self.user.username

class Tema(models.Model):
    titulo = models.CharField(max_length=255)
    mensaje = models.TextField(default='')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

class TemaForo(models.Model):
    titulo = models.CharField(max_length=255)
    mensaje = models.TextField(default='')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo + '-by ' + self.autor.username