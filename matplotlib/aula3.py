import matplotlib.pyplot as plt  # Importa o módulo para criar gráficos
import numpy as np  # Importa o módulo para trabalhar com arrays e cálculos matemáticos

# Gera 11 valores igualmente espaçados entre 0 e 5
x = np.linspace(0, 5, 11)

# Eleva cada valor de x ao quadrado, gerando os valores correspondentes de y
y = x**2

# Cria uma nova figura para o gráfico
fig = plt.figure()

# Adiciona um conjunto de eixos à figura
# O formato [esquerda, inferior, largura, altura] define a posição e tamanho do eixo em relação à figura
ax = fig.add_axes([0, 0, 1, 1])

# Plota os valores de x e y no eixo especificado
# color="blue" define a cor da linha
# lw=3 define a espessura da linha
# ls="--" define o estilo da linha (neste caso, tracejada)
ax.plot(
    x,
    y,
    color="blue",
    lw=3,
    ls="--",
)

# Define os limites do eixo x para que variem de 0 a 1
ax.set_xlim([0, 1])

# Define os limites do eixo y para que variem de 0 a 2
ax.set_ylim([0, 2])

# Exibe o gráfico na tela
plt.show()
