import numpy as np

# Cria um array NumPy com números de 0 a 10 (intervalo [0, 11), exclusivo no final)
arr = np.arange(0, 11)

# Indexação simples: retorna o elemento no índice 8 (resultado: 8)
arr[8]

# Fatiamento: retorna os elementos do índice 1 ao 4 (resultado: [1, 2, 3, 4])
arr[1:5]

# Fatiamento: retorna os elementos do índice 0 ao 5 (resultado: [0, 1, 2, 3, 4, 5])
arr[0:6]

# Fatiamento: retorna os elementos do índice 5 até o final do array (resultado: [5, 6, 7, 8, 9, 10])
arr[5:]

# Fatiamento com atribuição: altera os valores dos índices 0 a 4 para 100
arr[0:5] = 100  # O array passa a ser: [100, 100, 100, 100, 100, 5, 6, 7, 8, 9, 10]

# Recria o array original de 0 a 10, sobrescrevendo o anterior
arr = np.arange(0, 11)

# Fatiamento: pega os primeiros 6 elementos do array e armazena em `slice_of_arr`
slice_of_arr = arr[0:6]  # slice_of_arr = [0, 1, 2, 3, 4, 5]

# Cria uma cópia do array original; alterações em `copy_arr` não afetam `arr`
copy_arr = arr.copy()

# Cria um array bidimensional 3x3
arr_2d = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])

# Fatiamento 2D: retorna os elementos das 2 primeiras linhas (0 e 1),
# e das colunas a partir da segunda (colunas 1 e 2)
arr_2d[:2, 1:]  # Resultado: [[10, 15], [25, 30]]

# Cria um array de 1 a 10
arr2 = np.arange(1, 11)

# Cria um array booleano com a condição `arr2 > 5` (True onde o valor é maior que 5)
bool = arr2 > 5
print(
    bool
)  # Resultado: [False, False, False, False, False, True, True, True, True, True]

# Cria um array 2D com números de 0 a 49, com 5 linhas e 10 colunas
arr_2d = np.arange(50).reshape(5, 10)

# Fatiamento 2D: retorna as linhas de índice 1 e 2, com todas as colunas
arr_2d[1:3]  # Resultado: array([[10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
#               [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]])
