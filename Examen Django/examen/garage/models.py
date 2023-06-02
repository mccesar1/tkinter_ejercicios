from django.db import models

from participante.models import Participante


# Create your models here.

class Automovil(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)


    def __str__(self):
        return self.marca

class Caracteristica(models.Model):
    motor = models.CharField(max_length=100)
    peso = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    automovil = models.ForeignKey(Automovil, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Contrato(models.Model):

    #relacion a participante
    cliente = models.ForeignKey(Participante, on_delete=models.CASCADE)
    automovil = models.ForeignKey(Automovil, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre