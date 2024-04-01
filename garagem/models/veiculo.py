from django.db import models
from uploader.models import Image
from . import Marca, Categoria, Cor, Modelo, Acessorios
class Veiculo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="veiculo")
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name = "veiculo")
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name = "veiculo")
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, related_name = "veiculo")
    acessorios = models.ManyToManyField(Acessorios, related_name="veiculo")
    ano = models.IntegerField(null = True, default = 0)
    preco = models.DecimalField(max_digits = 10, decimal_places = 2, null = True, default = 0)
    imagem = models.ForeignKey(Image, related_name="+", on_delete=models.CASCADE, null=True, blank=True, default=None,)
    def __str__(self):
        return f"{self.marca} {self.modelo} {self.ano} {self.cor}"
    