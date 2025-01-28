import pandas as pd
import numpy as np

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('clientes_remove_outliers.csv')

print(df.head())
#Mascarar dados pessoais
df['cpf_mascara'] = df['cpf'].apply(lambda cpf: f'{cpf[:3]}.***.***-{cpf[-2:]}')

#Corrrigir datas
df['data'] = pd.to_datetime(df['data'], format='%Y=%m-%d', errors='coerce')

data_atual = pd.to_datetime('today')
df['data_atualizada'] = df['data'].where(df['data'] <= data_atual, pd.to_datetime('1900-01-01'))
df['idade_ajustada'] = data_atual.year - df['data_atualizada'].dt.year
df['idade_ajustada'] -=((data_atual.month <= df['data_atualizada'].dt.month) & (data_atual.day < df['data_atualizada'].dt.day)).astype(int)
df.loc[df['idade_ajustada'] > 100, 'idade_ajustada'] = np.nan

#Corrigir campo com múltiplas informações
# Substituir valores nulos por 'Desconhecido' e converter tudo para string
df['endereco'] = df['endereco'].fillna('Desconhecido').astype(str)

# Extrair o endereço curto
df['endereco_curto'] = df['endereco'].apply(lambda x: x.split('\n')[0].strip() if '\n' in x else x)

# Extrair o bairro
df['bairro'] = df['endereco'].apply(lambda x: x.split('\n')[1].strip() if '\n' in x else 'Desconhecido')

# Extrair o estado (sigla após " / ")
df['estado_sigla'] = df['endereco'].apply(lambda x: x.split(' / ')[-1].strip() if ' / ' in x else 'Desconhecido')

# Validar os estados com base na lista de siglas
estados_br = [
    "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA",
    "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN",
    "RS", "RO", "RR", "SC", "SP", "SE", "TO"
]

df['estado_sigla'] = df['estado_sigla'].str.upper().apply(lambda x: x if x in estados_br else 'Desconhecido')

# Resultado final
print('Dados tratados: \n', df.head())