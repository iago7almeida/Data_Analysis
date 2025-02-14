import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./ecommerce_estatistica.csv', encoding='utf-8')
#print(df.head())

# Análise exploratória de dados
print("Informações do Dataset:\n ")
print(df.info())
print(df.describe())
print(df.isnull().sum())
#df.fillna(df.mean(), inplace=True)
print("\n Top 10 produtos mais vendidos:")
print(df.nlargest(10, 'Qtd_Vendidos_Cod')[['Título', 'N_Avaliações', 'Marca', 'Preço', 'Gênero', 'Temporada']])
print("\nCorrelação entre preço e Vendas:")
corre = df['Preço'].corr(df['Qtd_Vendidos_Cod'])
print(f"Correlação: {corre:.2f}")
print("\nResumo do preço por Marca: ")
print(df.groupby('Marca')['Preço'].agg(['mean', 'median', 'count', 'std']))

# Gráfico de Histograma
plt.figure(figsize=(10,5))
sns.histplot(df['Preço'], bins=30, kde=True, color='blue', alpha=0.8)
plt.title('Distribuição de Preços dos Produtos')
plt.xlabel('Preço')
plt.ylabel('Frequência')
plt.show()

# gráfico de dispersão
plt.figure(figsize=(10,5))
sns.scatterplot(x=df['Preço'], y=df['Qtd_Vendidos_Cod'], alpha=0.5)
#sns.scatterplot(x=df['Preço'], y=df['N_Avaliações'], alpha=0.5) # comparando com o número de avaliações
plt.title('Dispersão entre preço e quantidade vendida')
plt.xlabel('Preço')
plt.ylabel('quantidade vendida')
plt.show()

# Mapa de calor
df_correlacao = df[['Preço', 'N_Avaliações', 'Nota', 'Qtd_Vendidos_Cod', 'Marca_Freq', 'Desconto', 'Marca_Cod', 'Material_Cod', 'Temporada_Cod', 'Marca_Freq', 'Material_Freq', 'Nota_MinMax', 'N_Avaliações_MinMax', 'Desconto_MinMax']].corr()
plt.figure(figsize=(10, 6))
sns.heatmap(df_correlacao, annot=True, cmap='coolwarm', fmt=".2f")
#sns.heatmap(df.corr(), annot=True, linewidths=0.5)
plt.title('Mapa de calor correlação entre variaveís númeriucas')
plt.show()

#Gráfico de barras
plt.figure(figsize=(12,6))
df.groupby('Marca')['Qtd_Vendidos_Cod'].sum().sort_values().head(30).plot(kind='bar', color='purple')
#df['Marca'].value_counts().plot(kind='bar', color='red')
plt.title('30 Marcas mais vendidas')
plt.xlabel('Marca')
plt.ylabel('Quantidade de produtos')
plt.xticks(rotation=65)
plt.show()

# Gráfico de pizza

plt.figure(figsize=(10,6))
#plt.pie(y, labels=x, autopct='%.1f%%', startangle=90)
#df['Gênero'].value_counts().plot(kind='pie', autopct='%1.1f%%')
df.groupby('Gênero')['Qtd_Vendidos_Cod'].sum().plot(kind='pie', autopct='%1.1f%%', cmap='viridis')
plt.title('Distribuição de vendas por genêro')
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1))
plt.show()

genero_vendas = df.groupby('Gênero')['Qtd_Vendidos_Cod'].sum()
genero_vendas = genero_vendas.sort_values(ascending=False)
explode = [0.1 if v > genero_vendas.sum() * 0.1 else 0 for v in genero_vendas]
genero_vendas.plot(kind='pie', autopct=lambda p: f'{p:.1f}%' if p > 3 else '', startangle=90, cmap='viridis', explode=explode, pctdistance=0.8, labeldistance=1.1)
plt.title('Distribuição de vendas por genêro')
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1))
plt.show()


# Gráfico de Densidade
plt.figure(figsize=(10,6))
sns.kdeplot(df['Qtd_Vendidos_Cod'], fill=True, color='gray')
plt.title('Densidade de quantidade de produtos vendidos')
plt.xlabel('Quantidade de produtos vendidos')
plt.ylabel('Densidade')
plt.show()
sns.kdeplot(df['Preço'], fill=True, color='gray')
plt.title('Densidade de preços')
plt.xlabel('Preço')
plt.ylabel('Densidade')
plt.show()

#Gráfico de regressão
plt.figure(figsize=(10, 5))
sns.regplot(data=df, x='Preço', y='Qtd_Vendidos_Cod', color='#278f65', scatter_kws={'alpha':0.5, 'color': 'red'})
plt.title('Regresssão entre Preço e Quantidade vendida')
plt.xlabel('Preço')
plt.ylabel('Quantidade vendida')
plt.show()