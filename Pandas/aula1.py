# Importando as bibliotecas necessárias
import numpy as np  # Importa a biblioteca NumPy, útil para manipulação de arrays
import pandas as pd  # Importa a biblioteca Pandas, utilizada para manipulação de dados estruturados como DataFrames e Series

# Definindo algumas variáveis para uso posterior
labels = ["a", "b", "c"]  # Uma lista de rótulos que servirão como índices
my_data = [
    10,
    20,
    30,
]  # Uma lista de dados, os valores que iremos usar para criar uma Series
arr = np.array(
    my_data
)  # Convertendo 'my_data' para um array do NumPy (para mostrar que podemos usar arrays também)
d = {
    "a": 10,
    "b": 20,
    "c": 30,
}  # Um dicionário com chaves como índices e valores como dados

# Criando uma Series com a lista de dados 'my_data' sem especificar um índice
print(
    pd.Series(data=my_data)
)  # O Pandas cria automaticamente um índice numérico (0, 1, 2) para os dados

# Criando uma Series com a lista de dados 'my_data' e usando a lista 'labels' como índice
print(
    pd.Series(data=my_data, index=labels)
)  # A lista 'labels' define os índices para os dados, então a Series será:
#    a    10
#    b    20
#    c    30

# Outra forma de criar a Series, apenas invertendo a ordem dos parâmetros (dados e índices)
print(
    pd.Series(my_data, labels)
)  # A mesma coisa que a linha anterior, mas com a ordem de argumentos trocada

# Criando uma Series a partir de um array NumPy 'arr' e usando 'labels' como índice
pd.Series(
    arr, labels
)  # Aqui, criamos a Series com os mesmos dados de 'my_data', mas a variável 'arr' é um array do NumPy

# Criando uma Series diretamente de um dicionário 'd'
pd.Series(
    d
)  # O dicionário é convertido automaticamente em uma Series, onde as chaves se tornam os índices:
#    a    10
#    b    20
#    c    30

# Exibindo o dicionário 'd' para ver a estrutura antes de convertê-lo em uma Series
print(d)  # Mostra o dicionário 'd' com suas chaves e valores

# Criando uma Series com dados numéricos e um índice personalizado de países
ser1 = pd.Series(
    [1, 2, 3, 4], ["USA", "Germany", "USSR", "Japan"]
)  # Dados são [1, 2, 3, 4] e os índices são países
print(
    ser1
)  # Exibe a Series com índices "USA", "Germany", "USSR" e "Japan", com os valores correspondentes [1, 2, 3, 4]

# Criando outra Series com dados e índices diferentes
ser2 = pd.Series(
    [1, 2, 5, 4], ["USA", "Germany", "Italy", "Japan"]
)  # Modifica o índice "USSR" para "Italy"
print(
    ser2
)  # Exibe a nova Series, com índices ["USA", "Germany", "Italy", "Japan"] e valores [1, 2, 5, 4]

# Criando uma Series a partir da lista 'labels', sem especificar índice (índice será numérico padrão)
ser3 = pd.Series(
    data=labels
)  # A lista 'labels' será usada como dados e o Pandas atribuirá um índice numérico padrão (0, 1, 2)
# O resultado será algo como:
# 0    a
# 1    b
# 2    c
