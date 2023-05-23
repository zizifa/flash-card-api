from rest_framework.serializers import ModelSerializer
from .models import FlashCard

class CreateFlashCardSerialize(ModelSerializer):
    class Meta:
        model = FlashCard
        fields='__all__'


class UpdateFlashCardSerialize(ModelSerializer):
    class Meta:
        model = FlashCard
        fields=('question','answer')


class ListFlashCardSerialize(ModelSerializer):
    class Meta:
        model = FlashCard
        fields='__all__'