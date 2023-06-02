from django.db import models

# Create your models here.
class Participante(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    sexo = models.CharField(max_length=100)
    edad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre