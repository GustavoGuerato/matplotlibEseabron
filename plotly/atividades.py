# Importação das bibliotecas necessárias para visualização de dados com Plotly e manipulação de dados com Pandas
import chart_studio.plotly as py  # Para integrar Plotly com notebooks e fazer upload de gráficos
import plotly.graph_objs as go  # Para criar gráficos usando objetos gráficos de Plotly
from plotly.offline import (
    download_plotlyjs,
    init_notebook_mode,
    plot,
    iplot,
)  # Para renderizar gráficos offline
import pandas as pd  # Para manipulação e análise de dados estruturados

# Carregamento do dataset '2014_World_Power_Consumption.csv' que contém dados sobre o consumo mundial de energia
df = pd.read_csv("2014_World_Power_Consumption")

# Remoção de espaços extras dos nomes das colunas, garantindo a consistência e evitando erros de referência
df.columns = df.columns.str.strip()

# Exibe as primeiras 5 linhas do dataframe para verificar a estrutura e o conteúdo dos dados carregados
print(df.head())

# Definição do dicionário de dados para criar um gráfico coroplético, representando o consumo de energia por país
data = dict(
    type="choropleth",  # Especifica o tipo de gráfico como coroplético (mapa de calor geográfico)
    locations=df["Country"],  # Define os países como localizações para o mapa
    locationmode="country names",  # Usa nomes de países como modo de localização
    z=df[
        "Power Consumption KWH"
    ],  # Dados que serão mapeados, o consumo de energia em KWH
    text=df[
        "Text"
    ],  # Informações adicionais que aparecerão como texto ao passar o mouse sobre os países
    colorbar={
        "title": "Power Consumption KWH"
    },  # Título da barra de cores que mostra a escala de consumo de energia
)

# Configuração do layout do gráfico, incluindo aspectos visuais e geográficos
layout = dict(
    title="2014 World Power Consumption",  # Título do gráfico
    geo=dict(
        showframe=False,  # Não exibir bordas ao redor do mapa
        showcoastlines=False,  # Não exibir linhas costeiras, para uma visualização mais limpa
        projection_type="equirectangular",  # Define o tipo de projeção do mapa como equiretangular
        showlakes=True,  # Exibe lagos no mapa para maior detalhe geográfico
    ),
)

# Criação do gráfico usando o objeto Figure de Plotly, combinando os dados e o layout
fig = go.Figure(data=[data], layout=layout)

# Exibe o gráfico de consumo mundial de energia como um mapa interativo
fig.show()

# Carregamento de um segundo dataset '2012_Election_Data.csv' contendo dados sobre a eleição de 2012 nos EUA
df2 = pd.read_csv("2012_Election_Data")

# Exibição das primeiras 5 linhas do dataframe para verificação inicial dos dados e confirmação de carregamento correto
print(df2.head())

# Conversão da coluna 'Voting-Age Population (VAP)' para o tipo float, assegurando que os dados são numéricos
df2["Voting-Age Population (VAP)"] = df2["Voting-Age Population (VAP)"].astype(float)

# Criação de um mapa coroplético para mostrar a População em Idade de Votar (VAP) por estado nos EUA
fig = go.Figure(
    data=go.Choropleth(
        locations=df2["State Abv"],  # Usa abreviações de estados como localizações
        z=df2[
            "Voting-Age Population (VAP)"
        ],  # Dados de VAP para a escala de cores do mapa
        locationmode="USA-states",  # Especifica que as localizações são estados dos EUA
        colorscale="Blues",  # Define uma escala de cores azuis para os dados
        colorbar_title="VAP",  # Título da barra de cores para o gráfico
    )
)

# Atualização do layout do gráfico para incluir título e configuração geográfica específica para os EUA
fig.update_layout(
    title_text="Voting-Age Population (VAP) por Estado",  # Define o título do gráfico
    geo_scope="usa",  # Limita o escopo geográfico do mapa para mostrar apenas os EUA
)

# Exibe o mapa coroplético de VAP por estado, proporcionando uma visualização interativa dos dados eleitorais
fig.show()
