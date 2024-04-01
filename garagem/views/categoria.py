from rest_framework.viewsets import ModelViewSet
from garagem.models import Categoria
from garagem.serializers import CategoriaSerializers

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializers