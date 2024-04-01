from rest_framework.viewsets import ModelViewSet
from garagem.models import Acessorios
from garagem.serializers import AcessoriosSerializers

class AcessoriosViewSet(ModelViewSet):
    queryset = Acessorios.objects.all()
    serializer_class = AcessoriosSerializers