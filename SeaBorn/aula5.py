# Importa as bibliotecas necessárias
import seaborn as sns
import matplotlib.pyplot as plt

# Carrega o conjunto de dados "tips" embutido no Seaborn
tips = sns.load_dataset("tips")
# Exibe as 5 primeiras linhas do DataFrame para inspeção
print(tips.head())

# Gráfico de regressão linear simples com distinção por gênero
sns.lmplot(
    x="total_bill",  # Define a coluna para o eixo X (total da conta)
    y="tip",  # Define a coluna para o eixo Y (gorjeta)
    data=tips,  # Define o DataFrame a ser usado
    hue="sex",  # Colore os pontos de acordo com o gênero (coluna "sex")
    markers=["o", "v"],  # Define os marcadores para cada gênero
    scatter_kws={
        "s": 100
    },  # Configurações do gráfico de dispersão (tamanho dos pontos)
)
# Exibe o gráfico
plt.show()

# Gráfico de regressão linear separado por dias da semana
sns.lmplot(
    x="total_bill",  # Coluna no eixo X
    y="tip",  # Coluna no eixo Y
    data=tips,  # DataFrame usado
    col="day",  # Cria subgráficos para cada valor único da coluna "day"
    hue="sex",  # Diferencia por gênero dentro de cada subplot
    aspect=0.5,  # Ajusta a largura dos subplots
    size=7,  # Define o tamanho dos subplots
)
# Exibe os gráficos
plt.show()
