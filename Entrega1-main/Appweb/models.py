from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Cartas(models.Model):
    nombre = models.CharField(max_length=60)
    precio = models.FloatField()
    imagen = models.ImageField(upload_to="cartas", null=True)
    stock = models.IntegerField()
    descripcion = models.CharField(max_length=500)
    artista = models.CharField(max_length=60)
    rareza = models.CharField(max_length=13)
    tipo = models.CharField(max_length=20)
    costo = models.IntegerField()
    def __str__(self):
        return f"Carta: {self.nombre}  - Precio: {self.precio} - Stock: {self.stock}"


class Avatar(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)


