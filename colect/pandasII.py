from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# Configurar o driver (use o ChromeDriver ou o geckodriver)
driver = webdriver.Chrome()

url = 'https://www.infomoney.com.br/cotacoes/b3/indice/ibovespa/historico/'
driver.get(url)

# Esperar a página carregar
import time
time.sleep(5)

# Pegar o HTML renderizado
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Extrair a tabela usando pandas
try:
    url_dados = pd.read_html(str(soup))
    print(url_dados[0].head(10))
except Exception as e:
    print("Erro ao acessar os dados:", e)

driver.quit()
