from rest_framework.serializers import ModelSerializer
from ..models import firstapp

class firstappSerializer(ModelSerializer):
    class Meta:
        model = firstapp
        fields = ('id', 'title', 'body')
