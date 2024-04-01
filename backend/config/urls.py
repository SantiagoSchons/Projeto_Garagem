from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from garagem.views import  AcessoriosViewSet, CategoriaViewSet, CorViewSet, MarcaViewSet, ModeloViewSet, VeiculoViewSet

router = DefaultRouter()
router.register(r"Acessorios", AcessoriosViewSet)
router.register(r"Categorias", CategoriaViewSet)
router.register(r"Cores", CorViewSet)
router.register(r"marcas", MarcaViewSet)
router.register(r"modelos", ModeloViewSet)
router.register(r"veiculos", VeiculoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
]
