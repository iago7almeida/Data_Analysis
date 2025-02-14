import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import dash
from dash import dcc, html, Input, Output

df = pd.read_csv('./ecommerce_estatistica.csv', encoding='utf-8')

app = dash.Dash(__name__)

# Layout
app.layout = html.Div([
    html.H1("Dashboard de Estatistica de E-commerce"),
    
    html.Label("Selecione a marca"),
    dcc.Dropdown(
        id='marca_selecionada',
        options=[{'label': marca, 'value': marca} for marca in df['Marca'].unique()],
        value=df['Marca'].unique()[0],
        multi=False
    ),
    
    dcc.Graph(id='histograma'),
    dcc.Graph(id='dispersao'),
    dcc.Graph(id='mapa_calor'),
    dcc.Graph(id='grafico_barra'),
    dcc.Graph(id='grafico_pizza'),
    dcc.Graph(id='densidade'),
    dcc.Graph(id='regressao')
])

@app.callback(
    [
        Output('histograma', 'figure'),
        Output('dispersao', 'figure'),
        Output('mapa_calor', 'figure'),
        Output('grafico_barra', 'figure'),
        Output('grafico_pizza', 'figure'),
        Output('densidade', 'figure'),
        Output('regressao', 'figure')
    ],
    [Input('marca_selecionada', 'value')]
)

def update_gragh(marca):
    df_filter = df[df['Marca'] == marca]
    
    # Gráfico Histograma
    hist_fig = px.histogram(df_filter, x='Nota', nbins=30, marginal='box', title='Distribuição das Notas')
    
    # Gráfico de dispersão
    disp_fig = px.scatter(df_filter, x='Preço', y='N_Avaliações', color='Desconto', title='Preço vs Número de Avaliações')
    
    # Mapa de Calor
    corr_matrix = df_filter[['Nota', 'N_Avaliações', 'Desconto', 'Preço']].corr()
    heatmap_fig = px.imshow(corr_matrix, title='Mapa de Calor das Correlações')
    
    # Gráfico de Barra
    barra_fig = px.bar(df_filter, x='Material', y='Qtd_Vendidos_Cod', color='Material', title='Quantidade Vendida por Material')
    
    # Gráfico de Pizza
    pizza_fig = px.pie(df_filter, names='Temporada', values='Qtd_Vendidos_Cod', title='Distribuição de Vendas por Temporada')
    
    # Gráfico de Densidade
    dens_fig = px.density_contour(df_filter, x='Preço', y='N_Avaliações', title='Densidade de Preço vs. Avaliações')
    
    # Gráfico de Regressão
    reg_fig = px.scatter(df_filter, x='Preço', y='Qtd_Vendidos_Cod', trendline='ols', title='Regressão de Preço vs. Quantidade Vendida')
    
    return hist_fig, disp_fig, heatmap_fig, barra_fig, pizza_fig, dens_fig, reg_fig

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)