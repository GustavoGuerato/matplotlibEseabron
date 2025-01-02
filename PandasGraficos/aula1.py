# Importação das bibliotecas necessárias para visualização e manipulação de dados
import pandas as pd  # Para manipulação de dados em DataFrames
import seaborn as sns  # Para visualizações estatísticas e gráficos
import matplotlib.pyplot as plt  # Para visualização gráfica
import numpy as np  # Para operações numéricas

# Carregando o primeiro DataFrame 'df1' com a coluna de índice definida como a primeira coluna
df1 = pd.read_csv("df1", index_col=0)
# Exibindo as primeiras 5 linhas do DataFrame 'df1'
print(df1.head())

# Carregando o segundo DataFrame 'df2' (sem índice)
df2 = pd.read_csv("df2")

# Exibindo o histograma da coluna "A" de 'df1' com 30 bins
df1["A"].hist(bins=30)

# Outra forma de exibir o histograma da coluna "A" de 'df1'
df1["A"].plot.hist()

# Criando um gráfico de área do DataFrame 'df2', com transparência (alpha = 0.4)
df2.plot.area(alpha=0.4)

# Criando um gráfico de barras empilhadas do DataFrame 'df2'
df2.plot.bar(stacked=True)

# Mais uma vez, exibe o histograma da coluna "A" de 'df1'
df1["A"].plot.hist()

# Exibindo um gráfico de linha da coluna "B" de 'df1', com largura de linha igual a 1
# O gráfico terá um tamanho de 12x3 polegadas
df1.plot(y="B", kind="line", figsize=(12, 3), lw=1)
# Exibe o gráfico
plt.show()

# Criando um gráfico de dispersão (scatter plot) entre as colunas "A" e "B" de 'df1'
# O tamanho dos pontos é baseado nos valores da coluna "C", multiplicados por 100
df1.plot.scatter(x="A", y="B", s=df1["C"] * 100)
# Exibe o gráfico
plt.show()

# Criando um gráfico boxplot para o DataFrame 'df2' (útil para ver distribuições e outliers)
df2.plot.box()
# Exibe o gráfico
plt.show()

# Gerando um DataFrame com 1000 linhas e 2 colunas ('a' e 'b') com valores aleatórios
df = pd.DataFrame(np.random.randn(1000, 2), columns=["a", "b"])
# Exibindo as primeiras 5 linhas do DataFrame gerado
print(df.head())

# Criando um gráfico hexbin, onde 'a' é no eixo x e 'b' no eixo y,
# mostrando a densidade de pontos por área (gridsize = 25)
df.plot.hexbin(x="a", y="b", gridsize=25)
