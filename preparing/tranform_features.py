import pandas as pd
import numpy as np
from scipy import stats

pd.set_option('display.width', None)

df = pd.read_csv('C:/Users/iago.almeida_pigz/Videos/Preparing_data/clientes-v2-tratados.csv')

print(df.head())

df['salario_log'] =np.log1p(df['salario']) #log1p é usado para evitar problemas com valor 0
print("\nDataFrame após tranfromação logaritmica no 'salario': \n", df.head())

#Transformação box Cox
df['salrio_boxcox'], _ = stats.boxcox(df['salario'] + 1)
print("\nDataFrame após tranfromação Box Cox no 'salario': \n", df.head())

#Codificação frequência para ''estado
estado_freq = df['estado'].value_counts() / len(df)
df['estado_freq'] = df['estado'].map(estado_freq)
print("\nDataFrame após codificação de frequência para estado: \n", df.head())

#Interações
df['interacao_idade_filhos'] = df['idade'] * df['numero_filhos']
print("\nDataFrame após interação entre idade e numero de filhos: \n", df.head())
