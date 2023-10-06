from rest_framework.viewsets import ModelViewSet
from ..models import firstapp
from .serializers import firstappSerializer

class firstappViewSet(ModelViewSet):
    queryset = firstapp.objects.all
    serializer_class = firstappSerializer
    