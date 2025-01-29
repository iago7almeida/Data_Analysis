import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('./clientes-v3-preparado.csv')
print(df.head().to_string())

#Gráfico de dispersão
sns.jointplot(x='idade', y='salario', data=df, kind='scatter')
plt.show()

# Gráfico de densidade
plt.figure(figsize=(10, 6))
sns.kdeplot(df['salario'], fill=True, color='#863e9c')
plt.title('Densidade de salários')
plt.xlabel('Salário')
plt.show()

# Gráfico de pairplot - Dispersão e histograma
sns.pairplot(df[['idade', 'salario', 'anos_experiencia', 'nivel_educacao']])
plt.show()

# Gráfico de regressão
sns.regplot(x='idade', y='salario', data=df, color='#278f65', scatter_kws={'alpha':0.5, 'color': '#34c289'})
plt.title('Regressão de Salário por idade')
plt.xlabel('Idade')
plt.ylabel('Salário')
plt.show()

# Gráfico countplot com hue
sns.countplot(x='estado_civil', hue='nivel_educacao', data=df, palette='pastel')
plt.xlabel('Estado Civil')
plt.ylabel('Qantidade Clientes')
plt.legend(title='Nível de educação')
plt.show()