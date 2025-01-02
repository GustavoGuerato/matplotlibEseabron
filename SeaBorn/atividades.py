import seaborn as sns
import matplotlib.pyplot as plt

# Configura o estilo visual do Seaborn para "whitegrid", que adiciona grades ao fundo
sns.set_style("whitegrid")

# Carrega o dataset "Titanic" embutido no Seaborn
titanic = sns.load_dataset("titanic")

# Exibe as primeiras 5 linhas do dataset para inspecionar os dados
titanic.head()

# Gráfico de dispersão (scatterplot) com densidades marginais para "fare" e "age"
sns.jointplot(x="fare", y="age", data=titanic)
plt.show()

# Explicação:
# - O eixo x representa "fare" (tarifa paga).
# - O eixo y representa "age" (idade).
# - As distribuições marginais de cada variável são exibidas nos histogramas das bordas.

# Histograma simples para a coluna "fare" (tarifa paga)
sns.histplot(titanic["fare"], bins=30, kde=False, color="red")
plt.show()

# Explicação:
# - O histograma divide os valores de "fare" em 30 intervalos (bins).
# - Mostra a frequência de passageiros em cada intervalo de tarifa.
# - `kde=False` desativa a curva de densidade suavizada.
# - `color="red"` altera a cor do histograma para vermelho.

# Boxplot para comparar a idade ("age") em diferentes classes sociais ("class")
sns.boxplot(x="class", y="age", data=titanic)
plt.show()

# Explicação:
# - O eixo x representa as classes sociais (First, Second, Third).
# - O eixo y representa as idades.
# - Cada boxplot mostra:
#   - Mediana (linha central),
#   - Quartis (limites da caixa),
#   - Outliers (pontos fora da caixa).

# Swarmplot para mostrar todas as observações de idade por classe social
sns.swarmplot(x="class", y="age", data=titanic)
plt.show()

# Explicação:
# - Cada ponto representa um passageiro.
# - Exibe a dispersão dos valores de idade dentro de cada classe.
# - Útil para identificar densidades locais e padrões de distribuição.

# Gráfico de contagem do número de passageiros por sexo
sns.countplot(x="sex", data=titanic)
plt.show()

# Explicação:
# - O eixo x mostra as categorias de sexo (male, female).
# - O eixo y mostra o número de passageiros em cada categoria.
# - Ideal para variáveis categóricas.

# Filtra apenas as colunas numéricas do DataFrame Titanic
numeric_titanic = titanic.select_dtypes(include=["number"])

# Explicação:
# - Remove colunas não numéricas (por exemplo, "sex", "class").
# - Garante que a matriz de correlação seja calculada apenas entre variáveis numéricas.

# Calcula a matriz de correlação para variáveis numéricas
correlation_matrix = numeric_titanic.corr()

# Explicação:
# - A correlação mede o grau de associação linear entre variáveis.
# - Valores variam de -1 (correlação negativa perfeita) a 1 (correlação positiva perfeita).
# - Zero indica nenhuma correlação.

# Heatmap para visualizar a matriz de correlação
sns.heatmap(correlation_matrix, cmap="coolwarm", annot=True, fmt=".2f")
plt.title("Matriz de Correlação do Titanic")
plt.show()

# Explicação:
# - `cmap="coolwarm"` aplica um gradiente de cores do azul ao vermelho.
# - `annot=True` exibe os valores da correlação diretamente no gráfico.
# - `fmt=".2f"` formata os valores com 2 casas decimais.

# FacetGrid para criar histogramas separados por sexo
g = sns.FacetGrid(
    data=titanic, col="sex"
)  # Divide o DataFrame em duas colunas com base no sexo
g.map(
    plt.hist, "age"
)  # Cria um histograma de "age" para cada subgrupo (masculino e feminino)
plt.show()

# Explicação:
# - Gera gráficos separados para homens e mulheres.
# - Mostra a distribuição de idade dentro de cada grupo.
# - Facilita comparações diretas entre os dois grupos.
