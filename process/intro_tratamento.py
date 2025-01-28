import pandas as pd

df = pd.read_csv('./clientes.csv')

print(df.head().to_string())

print(df.tail().to_string())

print('Qtd: ', df.shape)

print('Tipagem: \n', df.dtypes)

print('Valores nulos: \n', df.isnull().sum())