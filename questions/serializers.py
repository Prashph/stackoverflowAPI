from rest_framework.serializers import ModelSerializer
from .models import Data

class QuestionsSerializer(ModelSerializer):
    class Meta:
        model = Data
        fields= '__all__'
