from django.db import models
from .marca import Marca 
class Veiculo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="veiculo")
    