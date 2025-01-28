import pandas as pd
import numpy as np

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
df = pd.read_csv('./clientes-v3-preparado.csv')

print('Estatistica com pandas')
print('Média: ', df['salario'].mean())
print('Mediana: ', df['salario'].median())
print('Variância: ', df['salario'].var())
print('Desvio padrão: ', df['salario'].std())
print('Moda: ', df['salario'].mode()[0])
print('Mínimo: \n', df['salario'].min())
print('Quartis:\n', df['salario'].quantile([0.25, 0.5, 0.75]))
print('Máximo: ', df['salario'].max())
print('Contagem de não nulo: ', df['salario'].value_counts().sum())
print('Soma: ', df['salario'].sum())

#Estrutura de dados
print("\nColuna do DataFrame:\n", df['salario'])
print("Array do campo: ", df['salario'].values)

print('Estatística com numpy')
print("\nMédia com coluna:\n", np.mean(df['salario']))
print("Média com array: ", np.mean(df['salario'].values))

array_campo = df['salario'].values
print("Mediana: ", np.median(array_campo))
print("Variância: ", np.var(array_campo))
print("Desvio padrão: ", np.std(array_campo))
print("Mínimo: ", np.min(array_campo))
print("Quartis: \n", np.quantile(array_campo, [0.25, 0.5, 0.75]))
print("Porcentagem: \n", np.percentile(array_campo, [25, 50, 75]))
print("Mínimo: ", np.max(array_campo))
print("Contagem de não zeros: ", np.count_nonzero(array_campo))
print("Soma: ", np.sum(array_campo))