import numpy as np
import pandas as pd

# Criamos um dicionário com três colunas, algumas contendo valores NaN
d = {"A": [1, 2, np.nan], "B": [5, np.nan, np.nan], "C": [1, 2, 3]}

# Convertendo o dicionário em um DataFrame do Pandas
df = pd.DataFrame(d)

# Exibimos o DataFrame original
print(df)  # Mostra o DataFrame inicial com valores NaN

# Remove as colunas que contêm pelo menos um valor NaN
# axis=1 indica que estamos nos referindo a colunas
print(df.dropna(axis=1))  # Exibe o DataFrame sem as colunas que têm NaN

# Remove as linhas que têm menos de 'thresh' valores não-nulos
# thresh=2 significa que a linha precisa ter pelo menos 2 valores não-nulos para ser mantida
print(df.dropna(thresh=2))  # Exibe o DataFrame após aplicar a filtragem por linha

# Substitui os valores NaN pelos valores médios de suas respectivas colunas
# df.mean() calcula a média de cada coluna ignorando os NaNs
print(
    df.fillna(value=df.mean())
)  # Exibe o DataFrame com NaN preenchidos pelas médias das colunas
