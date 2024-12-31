import matplotlib.pyplot as plt
import numpy as np

# Criando valores para os eixos x e y
x = np.linspace(0, 5, 11)  # Gera 11 valores uniformemente espaçados entre 0 e 5
y = x**2  # Eleva cada valor de x ao quadrado

# Método funcional para plotar gráficos simples
plt.plot(x, y, "r-")  # Plota y em função de x com linha vermelha contínua
plt.xlabel("X Label")  # Adiciona rótulo ao eixo X
plt.ylabel("Y label")  # Adiciona rótulo ao eixo Y
plt.title("Title")  # Adiciona título ao gráfico
plt.show()  # Exibe o gráfico

# Criando subplots na mesma figura
plt.subplot(1, 2, 1)  # Cria o primeiro subplot (1 linha, 2 colunas, posição 1)
plt.plot(x, y, "r")  # Gráfico em vermelho

plt.subplot(1, 2, 2)  # Cria o segundo subplot (posição 2)
plt.plot(y, x, "b")  # Gráfico em azul

plt.show()  # Exibe os subplots

# Usando o método orientado a objetos para maior controle sobre os gráficos
fig = plt.figure()  # Cria uma nova figura
axes = fig.add_axes(
    [0.1, 0.1, 0.8, 0.8]
)  # Define posição e tamanho do eixo principal ([esquerda, baixo, largura, altura])
axes.plot(x, y)  # Plota y em função de x
axes.set_xlabel("X Label")  # Adiciona rótulo ao eixo X
axes.set_ylabel("Y Label")  # Adiciona rótulo ao eixo Y
axes.set_title("Title")  # Adiciona título ao gráfico

plt.show()  # Exibe o gráfico

# Criando gráficos aninhados com múltiplos eixos
fig = plt.figure()  # Cria uma nova figura
axes1 = fig.add_axes(
    [0.1, 0.1, 0.8, 0.8]
)  # Eixos principais ([esquerda, baixo, largura, altura])
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])  # Eixos secundários aninhados

axes1.plot(x, y)  # Plota y em função de x no gráfico principal
axes2.plot(y, x)  # Plota x em função de y no gráfico secundário

axes1.set_title("Larger Plot")  # Título do gráfico principal
axes2.set_title("Smaller Plot")  # Título do gráfico secundário

plt.show()  # Exibe os gráficos
