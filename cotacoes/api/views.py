from rest_framework import viewsets
from .models import Cotacao
from .serializers import CotacaoSerializer

class CotacaoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cotacao.objects.all().order_by('-data')
    serializer_class = CotacaoSerializer
