from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from uploader.router import router as uploader_router
from usuario.router import router as usuario_router
from rest_framework.routers import DefaultRouter
from garagem.views import  AcessoriosViewSet, CategoriaViewSet, CorViewSet, MarcaViewSet, ModeloViewSet, VeiculoViewSet
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView)
router = DefaultRouter()
router.register(r"Acessorios", AcessoriosViewSet)
router.register(r"Categorias", CategoriaViewSet)
router.register(r"Cores", CorViewSet)
router.register(r"marcas", MarcaViewSet)
router.register(r"modelos", ModeloViewSet)
router.register(r"veiculos", VeiculoViewSet)

urlpatterns = [
    path("api/", include(usuario_router.urls)),
    path("api/media/", include(uploader_router.urls)),
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
    
    # OpenAPI 3
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
