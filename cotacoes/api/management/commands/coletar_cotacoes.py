from django.core.management.base import BaseCommand
from api.utils import obter_cotacoes

class Command(BaseCommand):
    help = "Coleta cotações do dólar"

    def handle(self, *args, **kwargs):
        obter_cotacoes()
        self.stdout.write(self.style.SUCCESS("Cotações coletadas com sucesso"))
