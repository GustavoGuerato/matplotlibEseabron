import numpy as np
import pandas as pd

# Criando o primeiro DataFrame df1 com colunas A, B, C, D e índices de 0 a 3
df1 = pd.DataFrame(
    {
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    },
    index=[0, 1, 2, 3],
)

# Criando o segundo DataFrame df2 com índices de 4 a 7
df2 = pd.DataFrame(
    {
        "A": ["A4", "A5", "A6", "A7"],
        "B": ["B4", "B5", "B6", "B7"],
        "C": ["C4", "C5", "C6", "C7"],
        "D": ["D4", "D5", "D6", "D7"],
    },
    index=[4, 5, 6, 7],
)

# Criando o terceiro DataFrame df3 com índices de 8 a 11
df3 = pd.DataFrame(
    {
        "A": ["A8", "A9", "A10", "A11"],
        "B": ["B8", "B9", "B10", "B11"],
        "C": ["C8", "C9", "C10", "C11"],
        "D": ["D8", "D9", "D10", "D11"],
    },
    index=[8, 9, 10, 11],
)

# Concatenando os três DataFrames verticalmente (linhas), mantendo índices originais
print(pd.concat([df1, df2, df3]))

# Concatenando os DataFrames horizontalmente (colunas), alinhando pelas linhas
print(pd.concat([df1, df2, df3], axis=1))

# Criando o DataFrame 'left' com uma coluna de chave para realizar mesclagens (key)
left = pd.DataFrame(
    {
        "key": ["K0", "K1", "K2", "K3"],  # Chave que será usada para mesclagem
        "A": ["A0", "A1", "A2", "A3"],  # Coluna A
        "B": ["B0", "B1", "B2", "B3"],  # Coluna B
    }
)

# Criando o DataFrame 'right' também com uma coluna de chave correspondente
right = pd.DataFrame(
    {
        "key": ["K0", "K1", "K2", "K3"],  # Mesma chave do 'left'
        "C": ["C0", "C1", "C2", "C3"],  # Coluna C
        "D": ["D0", "D1", "D2", "D3"],  # Coluna D
    }
)

# Exibindo os DataFrames criados para mesclagem
print(left)
print(right)

# Realizando um merge interno (default) na coluna 'key'
# O resultado será a união das colunas onde as chaves são iguais
print(pd.merge(left, right, how="inner", on="key"))

# Criando DataFrames para mesclagem com múltiplas chaves
left1 = pd.DataFrame(
    {
        "key1": ["K0", "K0", "K1", "K2"],  # Primeira chave
        "key2": ["K0", "K1", "K0", "K1"],  # Segunda chave
        "A": ["A0", "A1", "A2", "A3"],  # Coluna A
        "B": ["B0", "B1", "B2", "B3"],  # Coluna B
    }
)

right1 = pd.DataFrame(
    {
        "key1": ["K0", "K1", "K1", "K2"],  # Primeira chave
        "key2": ["K0", "K0", "K0", "K0"],  # Segunda chave
        "C": ["C0", "C1", "C2", "C3"],  # Coluna C
        "D": ["D0", "D1", "D2", "D3"],  # Coluna D
    }
)

# Merge interno (apenas combinações que aparecem em ambos os DataFrames)
print(pd.merge(left1, right1, on=["key1", "key2"]))

# Merge externo (inclui todas as combinações possíveis, preenchendo valores ausentes com NaN)
print(pd.merge(left1, right1, how="outer", on=["key1", "key2"]))

# Criando DataFrames para demonstração do método 'join'
# Aqui os índices serão usados como chave
left2 = pd.DataFrame(
    {"A": ["A0", "A1", "A2"], "B": ["B0", "B1", "B2"]}, index=["K0", "K1", "K2"]
)

right2 = pd.DataFrame(
    {"C": ["C0", "C2", "C3"], "D": ["D0", "D2", "D3"]}, index=["K0", "K2", "K3"]
)

# Realizando uma junção (join) baseada nos índices dos DataFrames
# Por padrão, é um 'left join', ou seja, mantém os índices de 'left2'
print(left2.join(right2))
