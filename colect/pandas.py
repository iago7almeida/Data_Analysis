import requests
import pandas as pd

# URL do endpoint
url = 'https://www.infomoney.com.br/wp-json/infomoney/v1/quotes/history'

# Payload necessário (dados do formulário)
payload = {
    'page': 0,
    'numberItems': 50,
    'symbol': 'IBOVESPA'
}

# Cabeçalhos para simular um navegador
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
}

# Fazendo a requisição POST
response = requests.post(url, data=payload, headers=headers)

# Verificando o status da resposta
if response.status_code == 200:
    try:
        data = response.json()  # Convertendo para JSON
        
        # Convertendo os dados para DataFrame do pandas
        df = pd.DataFrame(data)
        
        # Mostrando os 5 primeiros registros
        print("Primeiros 5 registros do DataFrame:")
        print(df.head())
        
        # Exportar para CSV (opcional)
        df.to_csv('ibovespa_historico.csv', index=False)
        print("Dados exportados para 'ibovespa_historico.csv'.")
        
    except ValueError:
        print("Erro ao interpretar a resposta como JSON.")
else:
    print(f"Erro ao acessar: {response.status_code}")
