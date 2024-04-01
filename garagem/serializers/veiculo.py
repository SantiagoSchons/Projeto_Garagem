from rest_framework.serializers import ModelSerializer, SlugRelatedField
from garagem.models import Veiculo

from uploader.models import Image
from uploader.serializers import ImageSerializer

class VeiculoSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = "__all__"

    imagem_attachment_key = SlugRelatedField(source="imagem", queryset=Image.objects.all(), slug_field="attachment_key", required=False, write_only=True,)
    imagem = ImageSerializer(required=False, read_only=True)



class VeiculoDetailSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = "__all__"
        depth = 1
    livro = ImageSerializer(required=False)

class VeiculoListSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = ["id", "modelo", "ano"]