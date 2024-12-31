import seaborn as sns  # Importa a biblioteca seaborn para visualização de dados estatísticos.
import matplotlib.pyplot as plt  # Importa a biblioteca matplotlib para criar gráficos.

# Carrega o conjunto de dados "iris", que contém características de diferentes espécies de flores.
iris = sns.load_dataset("iris")
iris.head()  # Exibe as primeiras linhas do conjunto de dados para inspecionar sua estrutura.

# Cria um PairGrid para visualizar relações entre pares de variáveis do dataset "iris".
g = sns.PairGrid(iris)

# Mapeia diferentes tipos de gráficos para cada parte do PairGrid:
g.map_diag(
    sns.histplot
)  # Plota histogramas na diagonal (distribuição de cada variável individualmente).
g.map_upper(
    plt.scatter
)  # Plota gráficos de dispersão na parte superior (relações entre pares de variáveis).
g.map_lower(
    sns.kdeplot
)  # Plota gráficos de densidade na parte inferior (suavização das distribuições conjuntas).

plt.show()  # Exibe o gráfico.

# Carrega o conjunto de dados "tips", que contém informações sobre gorjetas em um restaurante.
tips = sns.load_dataset("tips")
print(
    tips.head()
)  # Exibe as primeiras linhas do dataset para inspecionar sua estrutura.

# Cria um FacetGrid para visualizar dados agrupados por duas categorias ("time" e "smoker").
g1 = sns.FacetGrid(data=tips, col="time", row="smoker")

# Mapeia gráficos de dispersão para cada faceta no grid:
g1.map(plt.scatter, "tip", "total_bill")
# Plota "tip" (gorjeta) no eixo x e "total_bill" (conta total) no eixo y para cada combinação de categorias.

plt.show()  # Exibe o gráfico.
