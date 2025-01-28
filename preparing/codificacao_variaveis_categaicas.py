import pandas as pd
from sklearn.preprocessing import LabelEncoder

pd.set_option('display.width', None)

df = pd.read_csv('C:/Users/iago.almeida_pigz/Videos/Preparing_data/clientes-v2-tratados.csv')

print(df.head())

#Codificação one-hot para 'estado_civil'
df = pd.concat([df, pd.get_dummies(df['estado_civil'], prefix='estado_civil')], axis=1)
print("\nDataFrame após codificação one-hot para estado civil: \n", df.head())

#Codificação ordinal para 'nivel_educacao'
educacao_ordem = {'Ensino Fundamental': 1, 'Ensino Médio': 2, 'Ensino Superior': 3, 'Pós-graduação':4}
df['nivel_educacao_ordinal'] = df['nivel_educacao'].map(educacao_ordem)

print("\nDataframe após codificação ordinal nivel educação: \n", df.head())

#Transformar 'area_atuacao' em categorias codificadas usando o método .cat.codes
df['area_atuacao_cod'] = df['area_atuacao'].astype('category').cat.codes
print("\nDataframe após tranformar area atuação em códigos númericos: \n", df.head())

#LabelEncoder para 'estado'
#LabelEncoder 
label_encoder = LabelEncoder()
df['estado_cod'] = label_encoder.fit_transform(df['estado'])

print("\nDataframe após aplicar LabelEncoder em 'estado': \n", df.head(30))
