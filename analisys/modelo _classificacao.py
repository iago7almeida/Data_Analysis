import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score
import joblib

df = pd.read_csv('./clientes-v3-preparado.csv')

#Categorizar salario: acima e abixo da mediana
df['salario_categoria'] = (df['salario'] > df['salario'].median()).astype(int) # 1 - acima da mediana, 0 - abaixo ou igual a mediana

X = df[['idade', 'anos_experiencia', 'nivel_educacao_cod', 'area_atuacao_cod']] # preditor
Y = df['salario_categoria'] # Prever

# Dividir dados: Treinamento e teste
X_train, X_teste, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Criar e treinar modelo - Regressão Logística
modelo_lr = LogisticRegression()
modelo_lr.fit(X_train, Y_train)

# Criar e treinar modelo - Árvore de decisão
modelo_dt = DecisionTreeClassifier()
modelo_dt.fit(X_train, Y_train)

# Prever valores de teste
Y_prev_lr = modelo_lr.predict(X_teste)
Y_prev_dt = modelo_dt.predict(X_teste)

# Métricas de avaliação - Regressão Logística
accuracy_lr = accuracy_score(Y_test, Y_prev_lr)
precision_lr = precision_score(Y_test, Y_prev_lr)
recall_lr = recall_score(Y_test, Y_prev_lr)

print(f'\nAcurácia da Regressão Logística: {accuracy_lr:.2f}')
print(f'Precisão da Regressão Logística: {precision_lr:.2f}')
print(f'Recall (Sencibilidade) da Regressão Logística: {recall_lr:.2f}')

# Métricas de avaliação - Árvore de decisão
acurracy_dt = accuracy_score(Y_test, Y_prev_dt)
precision_dt = precision_score(Y_test, Y_prev_dt)
recall_dt = recall_score(Y_test, Y_prev_dt)

print(f'\nAcurácia da Árvore de decisão: {acurracy_dt:.2f}')
print(f'Precisão da Árvore de decisão: {precision_dt:.2f}')
print(f'Recall (Sencibilidade) da Árvore de decisão: {recall_dt:.2f}')

#Salvar modelo
joblib.dump(modelo_lr, 'modelo_regressao_logistica.pkl')
joblib.dump(modelo_dt, 'modelo_arvore_decisao.pkl')

