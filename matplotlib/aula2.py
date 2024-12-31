import matplotlib.pyplot as plt
import numpy as np

# Cria um array com 11 números igualmente espaçados entre 0 e 5.
x = np.linspace(0, 5, 11)
# Cria um array 'y' onde cada elemento é o quadrado do elemento correspondente em 'x'.
y = x**2

# Cria uma figura.
fig = plt.figure()
# Adiciona eixos à figura. A lista [0.1, 0.1, 0.8, 0.8] representa a posição e o tamanho dos eixos:
# [esquerda, inferior, largura, altura], todos em coordenadas normalizadas da figura (0 a 1).
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

# Cria uma figura e um conjunto de subplots (gráficos menores dentro de um gráfico maior).
# nrows e ncols especificam o número de linhas e colunas de subplots.
fig, axes = plt.subplots(nrows=1, ncols=2)

# Plota 'x' versus 'y' no primeiro subplot (axes[0]).
axes[0].plot(x, y)
# Define o título do primeiro subplot.
axes[0].set_title("Primeiro Gráfico")

# Plota 'y' versus 'x' no segundo subplot (axes[1]).
axes[1].plot(y, x)
# Define o título do segundo subplot.
axes[1].set_title("Segundo Gráfico")

# Ajusta os parâmetros dos subplots para fornecer espaçamento entre eles, evitando sobreposição.
plt.tight_layout()

# Tamanho da Figura e DPI (Dots Per Inch - Pontos Por Polegada)

# Cria uma figura com 2 linhas e 1 coluna de subplots e define o tamanho da figura para 3 polegadas de largura e 2 polegadas de altura.
fig = plt.figure(nrows=2, ncols=1, figsize=(3, 2))
# Plota 'x' versus 'y' no primeiro subplot.
axes[0].plot(x, y)
# Plota 'y' versus 'x' no segundo subplot.
axes[1].plot(y, x)
# Salva a figura em um arquivo JPEG com uma resolução de 200 DPI.
# DPI (pontos por polegada) determina a resolução da imagem salva. Quanto maior o DPI, maior a resolução.
fig.savefig("minha_imagem.jpg", dpi=200)

# Cria uma nova figura.
fig = plt.figure()

# Adiciona eixos à figura que preenchem toda a área da figura (0 a 1 em todas as direções).
ax = fig.add_axes([0, 0, 1, 1])
# Plota 'x' versus 'y' com um rótulo "X ao Quadrado" para a legenda.
ax.plot(x, y, label="X ao Quadrado")
# Plota 'y' versus 'x' com um rótulo "X ao Cubo" para a legenda.
# Nota: o nome "X ao Cubo" pode ser confuso, já que o gráfico plota y (que é x²) versus x.
# Talvez fosse melhor outro nome ou plotar outra função de x, como x**3.
ax.plot(y, x, label="Y vs X")  # Rótulo mais adequado
# Exibe a legenda. loc=0 significa "melhor" localização, permitindo que o matplotlib escolha o melhor posicionamento automaticamente.
ax.legend(loc=0)

# Define o título dos eixos.
ax.set_title("Título")
# Define o rótulo do eixo x.
ax.set_xlabel("X")
# Define o rótulo do eixo y.
ax.set_ylabel("Y")

plt.show()  # Exibe todos os gráficos criados. Essencial para visualização.
