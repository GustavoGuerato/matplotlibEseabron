# Importando as bibliotecas necessárias
import matplotlib.pyplot as plt
import numpy as np

# Definindo os dados para o primeiro gráfico
x = np.linspace(0, 5, 100)  # Gerando 100 pontos entre 0 e 5
y = x  # y é igual a x (gráfico linear)

# Criando um gráfico simples
fig, ax = plt.subplots()  # Criando a figura e os eixos

ax.plot(x, y)  # Plotando o gráfico com os dados x e y
plt.show()  # Exibindo o gráfico


# Definindo uma nova figura com tamanho 5x5 polegadas
fig = plt.figure(figsize=(5, 5))

# Adicionando um gráfico aos eixos na posição especificada [left, bottom, width, height]
ax = fig.add_axes([0.1, 0.8, 0.2, 0.2])
ax.set_xlim(0, 1)  # Definindo os limites do eixo X
ax.set_ylim(0, 1)  # Definindo os limites do eixo Y
plt.show()  # Exibindo o gráfico


# Dados para o gráfico de quadrado
x = np.arange(0, 101)  # Gerando números de 0 a 100
y = x**2  # y = x^2 (função quadrática)

# Criando o gráfico principal
fig, ax = plt.subplots()  # Criando a figura e os eixos
ax.plot(x, y)  # Plotando a função quadrática

# Adicionando rótulos e limites aos eixos
ax.set_xlabel("X")  # Rótulo para o eixo X
ax.set_ylabel("Z")  # Rótulo para o eixo Y
ax.set_xlim(0, 100)  # Limite para o eixo X
ax.set_ylim(0, 10000)  # Limite para o eixo Y

# Adicionando um gráfico menor (inset) dentro do gráfico principal
inset_ax = fig.add_axes([0.35, 0.55, 0.2, 0.2])  # Posição e tamanho do gráfico menor

# Dados para o gráfico menor (zoom)
x_zoom = np.arange(
    20, 22.1, 0.1
)  # Gerando números entre 20 e 22 com espaçamento de 0.1
y_zoom = x_zoom**2  # Calculando o quadrado dos valores de x

# Plotando o gráfico menor
inset_ax.plot(x_zoom, y_zoom)
inset_ax.set_xlabel("X")  # Rótulo para o eixo X no gráfico menor
inset_ax.set_ylabel("Y")  # Rótulo para o eixo Y no gráfico menor
inset_ax.set_xlim(20, 22)  # Limites para o eixo X do gráfico menor
inset_ax.set_ylim(30, 50)  # Limites para o eixo Y do gráfico menor
inset_ax.set_title("Zoom")  # Título para o gráfico menor

plt.show()  # Exibindo o gráfico


# Criando múltiplos gráficos (subplots)
x = np.arange(0, 101)  # Dados para o eixo X
y1 = x * 2  # Dados para o primeiro gráfico (função linear)
y2 = x**2  # Dados para o segundo gráfico (função quadrática)

# Criando dois subgráficos lado a lado
fig, (ax1, ax2) = plt.subplots(
    1, 2, figsize=(10, 5)
)  # Subgráficos em 1 linha e 2 colunas

# Plotando o primeiro gráfico (linha azul)
ax1.plot(
    x, y1, linestyle="--", color="blue", linewidth=3
)  # Gráfico com linha azul tracejada
ax2.plot(x, y2, color="red", linewidth=3)  # Gráfico com linha vermelha sólida

# Removendo os ticks dos eixos para ambos os subgráficos
ax1.set_xticks([])  # Remover os ticks no eixo X do primeiro gráfico
ax1.set_yticks([])  # Remover os ticks no eixo Y do primeiro gráfico
ax2.set_xticks([])  # Remover os ticks no eixo X do segundo gráfico
ax2.set_yticks([])  # Remover os ticks no eixo Y do segundo gráfico

# Definindo limites para o segundo gráfico
ax2.set_ylim(0, 10000)  # Limite do eixo Y para o gráfico quadrático

# Ajustando o layout para evitar sobreposição
plt.tight_layout()
plt.show()  # Exibindo os gráficos


# Criando novamente gráficos lado a lado, agora com rótulos
x = np.arange(0, 101)
y1 = x * 2
y2 = x**2

# Criando os subgráficos lado a lado
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Plotando o gráfico linear
ax1.plot(x, y1, color="blue", linewidth=3)

# Plotando o gráfico quadrático
ax2.plot(x, y2, linestyle="--", color="red", linewidth=3)

# Adicionando rótulos aos eixos para ambos os gráficos
ax1.set_xlabel("x")  # Rótulo do eixo X para o primeiro gráfico
ax1.set_ylabel("y")  # Rótulo do eixo Y para o primeiro gráfico
ax2.set_xlabel("x")  # Rótulo do eixo X para o segundo gráfico
ax2.set_ylabel("z")  # Rótulo do eixo Y para o segundo gráfico

# Ajustando o limite do eixo Y para o segundo gráfico
ax2.set_ylim(0, 10000)

# Ajustando o layout para uma melhor visualização
plt.tight_layout()

# Exibindo o gráfico final
plt.show()
 