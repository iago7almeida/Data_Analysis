import requests
from bs4 import BeautifulSoup

url = 'https://wiki.python.org.br/AprendaMais'
requisicao = requests.get(url)
extracao = BeautifulSoup(requisicao.text, 'html.parser')

#print(extracao.text.strip())

for linha_texto in extracao.find_all('h2'):
    titulo = linha_texto.text.strip()
    print('Titulo: ', titulo)