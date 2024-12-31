import numpy as np

# Cria uma lista simples
my_list = [1, 2, 3]

# Converte a lista para um array NumPy
arr = np.array(my_list)
print(arr)  # Resultado: [1 2 3]

# Cria uma lista 2D (matriz) e a converte em um array NumPy 2D
my_mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
test = np.array(my_mat)
print(test)
# Resultado:
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

# Cria um array com números inteiros de 0 a 10, pulando de 2 em 2
np.arange(0, 11, 2)  # Resultado: [0 2 4 6 8 10]

# Cria um array de zeros com 3 elementos
np.zeros(3)  # Resultado: [0. 0. 0.]

# Cria uma matriz 5x5 de zeros
np.zeros((5, 5))
# Resultado:
# [[0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]]

# Cria uma matriz 3x5 de uns
np.ones((3, 5))
# Resultado:
# [[1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]]

# Cria 1000 números igualmente espaçados entre 0 e 5
np.linspace(0, 5, 1000)  # Exemplo: [0. 0.005 0.01 ... 4.99 5.]

# Cria uma matriz identidade 4x4
np.eye(4)
# Resultado:
# [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]
#  [0. 0. 1. 0.]
#  [0. 0. 0. 1.]]

# Gera uma matriz 5x5 de números aleatórios uniformemente distribuídos entre 0 e 1
teste = np.random.rand(5, 5)
# print(teste)  # Resultado: Matriz 5x5 com valores aleatórios (não determinístico)

# Gera uma matriz 3x9 de números aleatórios de uma distribuição normal (média 0, desvio padrão 1)
random = np.random.randn(3, 9)
# print(random)  # Resultado: Matriz 3x9 com valores aleatórios (não determinístico)

# Cria um array de 26 números consecutivos de 0 a 25
arr = np.arange(26)

# Gera um array de 10 números inteiros aleatórios entre 0 e 49
rarr = np.random.randint(0, 50, 10)
# Exemplo: [12 45 3 27 49 18 5 39 23 8] (valores variam a cada execução)

# Redimensiona o array `arr` para 5x5 (exige que o tamanho total seja consistente)
arr.reshape(5, 5)
# Resultado:
# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]
#  [15 16 17 18 19]
#  [20 21 22 23 24]]

# Retorna o valor máximo no array `rarr`
rarr.max()  # Exemplo: 49 (valor mais alto no array aleatório)

# Retorna o índice do valor máximo no array `rarr`
rarr.argmax()  # Exemplo: 4 (índice onde está o valor máximo)

# Retorna o valor mínimo no array `rarr`
rarr.min()  # Exemplo: 3 (valor mais baixo no array aleatório)

# Retorna novamente o índice do valor máximo (duplicado por engano no código)
rarr.argmax()  # Mesmo comportamento explicado antes
