import numpy as np
import pandas as pd
from numpy.random import randn

# Criação de índices hierárquicos
outside = ["G1", "G1", "G1", "G2", "G2", "G2"]  # Nível externo do índice
inside = [1, 2, 3, 1, 2, 3]  # Nível interno do índice
hier_index = list(zip(outside, inside))  # Combina os dois níveis em tuplas
hier_index = pd.MultiIndex.from_tuples(
    hier_index
)  # Cria um índice hierárquico (MultiIndex)

# Criação do DataFrame com números aleatórios
df = pd.DataFrame(
    randn(6, 2), hier_index, ["A", "B"]
)  # DataFrame com índice hierárquico e colunas 'A' e 'B'

# Seleção de uma linha específica
# Primeiro seleciona o grupo "G1", depois seleciona a linha com índice interno 1
df.loc["G1"].loc[1]

# Nomeando os níveis do índice para facilitar a interpretação
df.index.names = ["Groups", "Num"]  # Nível externo é 'Groups', e o interno é 'Num'

# Acessando um valor específico
# Seleciona o grupo "G1", depois a linha com índice interno 3, e finalmente o valor da coluna "B"
print(df.loc["G1"].loc[3]["B"])

# Usando o método xs para selecionar dados de um nível específico
# Aqui, seleciona todas as linhas onde o nível 'Num' é 1, independente do grupo
df.xs(1, level="Num")
