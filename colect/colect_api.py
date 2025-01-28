import requests

def enviar_arquivo():
    caminho = 'C:/Users/iago.almeida_pigz/Downloads/produtos_informatica.xlsx'
    
    requisicao = requests.post('https://file.io', files={'file': open(caminho, 'rb')})
    saida_requisicao = requisicao.json()
    
    print(saida_requisicao)
    url = saida_requisicao['link']
    print("Arquivo enviado. Link para acesso: ", url)
    



def receber_arquivo(file_url):
    requisicao = requests.get(file_url)

    if requisicao.ok:
        with open('arquivo_baixado.xlsx', 'wb') as file:
            file.write(requisicao.content)
        print("Arquivo baixado com sucesso")
    else:
        print("Erro nessa porra")
        
receber_arquivo('https://file.io/Y28sAFDQqjmc')


def enviar_arquivo_chave():
    caminho = 'C:/Users/iago.almeida_pigz/Downloads/produtos_informatica.xlsx'
    chave_acesso = 'SGL4GQ2.EXF3474-Z3QM55E-H30SKCR-1KD5GNN'
    
    requisicao = requests. post(
        'https://file.io',
        files={'file': open(caminho, 'rb')},
        headers={'Authorization': chave_acesso}
    )
    saida_requisicao = requisicao.json()
    
    print(saida_requisicao)
    url = saida_requisicao['link']
    print("Arquivo enviado com chave. link para ecesso: ", url)
    
#enviar_arquivo()
#enviar_arquivo_chave()