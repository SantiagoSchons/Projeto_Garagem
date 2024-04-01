from django.contrib import admin

from .models import Acessorios, Categoria, Cor, Marca, Modelo, Veiculo

admin.site.register(Acessorios)
admin.site.register(Categoria)
admin.site.register(Cor)
admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(Veiculo)


