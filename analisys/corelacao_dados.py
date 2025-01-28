import pandas as pd
import numpy as np

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
df = pd.read_csv('./clientes-v3-preparado.csv')

#uso do pandas
print('Estatistíca do datafrmae: \n', df.describe())

print('Estatística de um campo: \n', df[['salario', 'anos_experiencia']].describe())

print('Correlação: \n', df[['salario', 'idade']].corr())
print('Correlação com normalização: \n', df[['salarioMinMaxScaler', 'idadeMinMaxScaler']].corr())
print('Correlação com padronização: \n', df[['salarioStandardScaler', 'idadeStandardScaler']].corr())
print('Correlação com padronização: \n', df[['salarioRobustScaler', 'idadeRobustScaler']].corr())

print('Correlação: \n', df[['salario', 'idade', 'idadeMinMaxScaler', 'idadeStandardScaler', 'idadeRobustScaler']].corr())

df_filtro_idade = df[df['idade'] < 65]
print('Correlação de clientes menores de 65 anos: \n', df_filtro_idade[['salario', 'idade']].corr())

#Variável spúria - aumenta com o tempo
df['variavel_espuria'] = np.arange(len(df))

print('Variável espúria', df['variavel_espuria'].values)

person_corr = df[['salario', 'idade', 'anos_experiencia', 'idade_anos_experiencia_interac', 'numero_filhos', 'nivel_educacao_cod', 'area_atuacao_cod', 'estado_cod', 'variavel_espuria']].corr()
# Calculando a correlação de Spearman
spearman_corr = df[['salario', 'idade', 'anos_experiencia', 'idade_anos_experiencia_interac', 'numero_filhos', 'nivel_educacao_cod', 'area_atuacao_cod', 'estado_cod', 'variavel_espuria']].corr(method = "spearman")
print('\nCorrelação de pearson: \n', person_corr)
print('\nCorrelação de Spearman: \n', spearman_corr)