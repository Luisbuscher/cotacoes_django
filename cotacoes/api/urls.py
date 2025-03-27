from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CotacaoViewSet

router = DefaultRouter()
router.register(r'cotacoes', CotacaoViewSet, basename='cotacao')

urlpatterns = [
    path('', include(router.urls)),
]
