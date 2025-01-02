import seaborn as sns  # Importa a biblioteca Seaborn para visualização de dados
import matplotlib.pyplot as plt  # Importa a biblioteca Matplotlib para personalização e exibição de gráficos

# Carregando o conjunto de dados "tips" incluído no Seaborn
tips = sns.load_dataset("tips")  
# Este conjunto de dados contém informações sobre gorjetas em um restaurante, incluindo:
# total_bill (valor total da conta), tip (gorjeta), sex (sexo do cliente),
# smoker (se é fumante ou não), day (dia da semana), time (almoço ou jantar) e size (tamanho do grupo).

# Exibe as 5 primeiras linhas do DataFrame para entender a estrutura dos dados
tips.head()

# Configuração do contexto do estilo do gráfico para 'notebook'
# Isso ajusta o tamanho e o design dos gráficos para facilitar a visualização em notebooks.
sns.set_context("notebook")  

# Criação de um gráfico de contagem para a coluna 'sex'
sns.countplot(x="sex", data=tips)  
# Esse gráfico mostra o número de observações para cada categoria (masculino e feminino).

# Remove bordas superiores e direitas do gráfico para melhorar a estética
sns.despine()

# Exibe o gráfico de contagem
plt.show()

# Criação de um gráfico de regressão linear com dispersão para as variáveis 'total_bill' e 'tip'
sns.lmplot(
    x="total_bill",  # Eixo X: valor total da conta
    y="tip",         # Eixo Y: valor da gorjeta
    data=tips,       # Conjunto de dados utilizado
    hue="sex",       # Diferencia os pontos por cor com base no sexo
    palette="seismic"  # Esquema de cores (seismic: gradiente de azul a vermelho)
)
# Este gráfico mostra a relação entre o valor da conta e o valor da gorjeta, destacando homens e mulheres.

# Exibe o gráfico de regressão
plt.show()
