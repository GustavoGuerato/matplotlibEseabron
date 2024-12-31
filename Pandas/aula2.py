import numpy as np
import pandas as pd
from numpy.random import randn

# Definindo a semente para reprodutibilidade dos resultados aleatórios
np.random.seed(101)

# Criando um DataFrame com 5 linhas e 4 colunas de números aleatórios
df = pd.DataFrame(randn(5, 4), ["A", "B", "C", "D", "E"], ["W", "X", "Y", "Z"])
print(df)  # Exibe o DataFrame original

# Selecionando a coluna "W"
print(df["W"])

# Selecionando as colunas "W" e "Z"
print(df[["W", "Z"]])

# Exibindo o DataFrame original novamente
print(df)

# Removendo a linha "E" (axis=0 se refere às linhas, enquanto axis=1 se referiria às colunas)
df = df.drop("E", axis=0)
print(df)

# Exibindo a forma do DataFrame (número de linhas e colunas)
print(df.shape)

# Selecionando a linha "A" usando loc (baseado no rótulo da linha)
print(df.loc["A"])

# Selecionando a linha de índice 2 usando iloc (baseado no índice da linha)
print(df.iloc[2])

# Selecionando as linhas "A" e "B" e as colunas "W" e "Y"
print(df.loc[["A", "B"], ["W", "Y"]])

# Criando um DataFrame booleano onde as células são True se o valor for maior que 0
booldf = df > 0

# Selecionando as células que atendem à condição (valores > 0)
print(df[booldf])

# Outra forma de selecionar células com valor > 0
print(df[df > 0])

# Selecionando as linhas onde a coluna "W" é maior que 0
print(df[df["W"] > 0])

# Selecionando as linhas onde a coluna "Z" é menor que 0
print(df[df["Z"] < 0])

# Filtrando as linhas onde a coluna "W" > 0 e exibindo a coluna "X"
resultdf = df[df["W"] > 0]
print(resultdf["X"])

# Filtrando as linhas onde a coluna "W" > 0 e selecionando as colunas "Y" e "X"
print(df[df["W"] > 0][["Y", "X"]])

# Criando uma Série booleana para a coluna "W" > 0
boolser = df["W"] > 0

# Filtrando as linhas usando a Série booleana e selecionando as colunas "Y" e "X"
results = df[boolser]
MyCols = ["Y", "X"]
print(results[MyCols])

# Filtrando as linhas onde "W" > 0 ou "Y" > 1
print(df[(df["W"] > 0) | (df["Y"] > 1)])

# Resetando o índice (restaurando o índice numérico padrão)
print(df.reset_index())

# Criando uma lista de novos índices
newind = "CA NY WY OR CO".split()

# Atribuindo os novos índices ao DataFrame
df["States"] = newind

# Definindo a coluna "States" como o novo índice do DataFrame
df = df.set_index("States")
print(df)  # Exibe o DataFrame com o novo índice
