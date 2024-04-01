from rest_framework.serializers import ModelSerializer
from garagem.models import Acessorios

class AcessoriosSerializers(ModelSerializer):
    class Meta:
        model = Acessorios
        fields = "__all__"


