import pandas as pd
from sklearn.preprocessing import RobustScaler, MinMaxScaler, StandardScaler

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('C:/Users/iago.almeida_pigz/Videos/Preparing_data/clientes-v2-tratados.csv')

print(df.head())

df = df.drop(['data', 'estado', 'nivel_educacao', 'numero_filhos', 'estado_civil', 'area_atuacao'], axis=1)

#Normalização - MinMaxSacaler
scaler = MinMaxScaler()
df['idadeMinScaler'] = scaler.fit_transform(df[['idade']])
df['salarioMinScaler'] = scaler.fit_transform(df[['salario']])

min_max_scaler = MinMaxScaler(feature_range=(-1, 1))
df['idadeMinScaler_mm'] = min_max_scaler.fit_transform(df[['idade']])
df['salarioMinScaler_mm'] = min_max_scaler.fit_transform(df[['salario']])

#padronizaçãoo - StandScaler
scaler = StandardScaler()
df['idadeStandScaler'] = scaler.fit_transform(df[['idade']])
df['salarioStandScaler'] = scaler.fit_transform(df[['salario']])

#Padronização RobustScaler
scaler = RobustScaler()
df['idadeRobustScaler'] = scaler.fit_transform(df[['idade']])
df['salarioRobustScaler'] = scaler.fit_transform(df[['salario']])


print(df.head(15))

print("MinMaxSacler (De 0 a 1):")
print("Idade - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std: {:.4f}".format(df['idadeMinScaler'].min(), df['idadeMinScaler'].max(), df['idadeMinScaler'].mean(), df['idadeMinScaler'].std()))
print("Salario - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std: {:.4f}".format(df['salarioMinScaler'].min(), df['salarioMinScaler'].max(), df['salarioMinScaler'].mean(), df['salarioMinScaler'].std()))