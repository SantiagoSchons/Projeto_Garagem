from django.db import models
from . import Categoria, Marca

class Modelo(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete = models.PROTECT, related_name = "modelo")
    marca = models.ForeignKey(Marca, on_delete = models.PROTECT, related_name = "modelo")
    nome = models.CharField(max_length= 100)

    def __str__(self):
        return f"{self.nome}"