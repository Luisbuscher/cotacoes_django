import requests
from datetime import datetime, timedelta
from .models import Cotacao

def obter_cotacoes():
    moedas = ["BRL", "EUR", "JPY"]  # Moedas que vou coletar
    base_url = "https://api.vatcomply.com/rates"

    hoje = datetime.today()
    
    for i in range(5):  # Busca as cotacoes dos ukdltimos 5 dias
        data = (hoje - timedelta(days=i)).strftime("%Y-%m-%d")
        response = requests.get(f"{base_url}?base=USD&date={data}")

        if response.status_code == 200:
            rates = response.json().get("rates", {})
            for moeda in moedas:
                if moeda in rates:
                    Cotacao.objects.update_or_create(
                        data=data, moeda=moeda,
                        defaults={"valor": rates[moeda]}
                    )