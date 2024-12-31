import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Carrega o conjunto de dados "tips", que contém informações sobre gorjetas.
# As colunas incluem: total_bill (valor total da conta), tip (gorjeta), sex (gênero do cliente),
# smoker (se o cliente fuma ou não), day (dia da semana), time (horário - almoço ou jantar) e size (tamanho da mesa).
tips = sns.load_dataset("tips")

# Exibe as primeiras 5 linhas do conjunto de dados para inspecionar seu conteúdo.
tips.head()

# **Barplot**: Gráfico de barras
# Exibe o desvio padrão de "total_bill" (valor total da conta) agrupado por "sex" (gênero).
# Por padrão, o barplot usa a média como estimador, mas aqui usamos np.std para mostrar a variação (desvio padrão).
sns.barplot(x="sex", y="total_bill", data=tips, estimator=np.std)

# Exibe o gráfico
plt.show()

# **Countplot**: Gráfico de contagem
# Conta o número de ocorrências de cada categoria na variável "sex".
# Mostra a proporção de clientes masculinos e femininos no conjunto de dados.
sns.countplot(x="sex", data=tips)

# Exibe o gráfico
plt.show()

# **Boxplot**: Gráfico de caixa
# Mostra a distribuição de "total_bill" para cada categoria de "day" (dia da semana).
# Exibe informações como:
# - Quartil inferior (25%)
# - Mediana (50%)
# - Quartil superior (75%)
# - Valores atípicos (outliers), representados por pontos fora das "caixas".
sns.boxplot(x="day", y="total_bill", data=tips)

# Exibe o gráfico
plt.show()

# **Violinplot**: Combinação de KDE e Boxplot
# Mostra a distribuição de "total_bill" para cada "day".
# O parâmetro hue="sex" separa os dados por gênero, e split=True sobrepõe os valores masculino e feminino.
sns.violinplot(x="day", y="total_bill", data=tips, hue="sex", split=True)

# Exibe o gráfico
plt.show()

# **Stripplot**: Gráfico de dispersão categórica
# Exibe cada ponto individual de "total_bill" para cada "day".
# Os pontos representam os valores reais de "total_bill", enquanto a variável hue="sex" colore os pontos por gênero.
sns.stripplot(
    x="day",  # Categoria no eixo x (dia da semana)
    y="total_bill",  # Valores contínuos no eixo y (conta total)
    data=tips,  # Conjunto de dados
    hue="sex",  # Colore os pontos de acordo com o gênero
)

# Exibe o gráfico
plt.show()

# **Combinação de gráficos**: Violinplot + Swarmplot
# 1. O violinplot mostra a distribuição geral de "total_bill" por "day" usando KDE (em preto).
# 2. O swarmplot adiciona os pontos individuais sobre o violinplot, ajustando-os para evitar sobreposição.
sns.violinplot(
    x="day",  # Categoria no eixo x (dia da semana)
    y="total_bill",  # Valores contínuos no eixo y (conta total)
    data=tips,  # Conjunto de dados
    color="black",  # Define a cor do violinplot como preto
)

# O swarmplot coloca os valores individuais ajustados sobre o violinplot.
sns.swarmplot(
    x="day",  # Categoria no eixo x
    y="total_bill",  # Valores contínuos no eixo y
    data=tips,  # Conjunto de dados
)

# Exibe o gráfico
plt.show()
