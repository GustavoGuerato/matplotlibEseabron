import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Carrega o conjunto de dados "tips", que contém informações sobre gorjetas.
tips = sns.load_dataset("tips")
# Exibe as primeiras linhas do DataFrame para inspecionar os dados.
tips.head()

# Visualização da distribuição da variável "total_bill" (valor total da conta).
# A opção kde=True adiciona a estimativa de densidade kernel (KDE) à visualização.
# bins=40 define o número de bins no histograma.
sns.displot(tips["total_bill"], kde=True, bins=40)
plt.show()

# Gráfico conjunto mostrando a relação entre "total_bill" (conta total) e "tip" (gorjeta).
# Exibe um gráfico de dispersão e, nas margens, as distribuições das variáveis.
sns.jointplot(x="total_bill", y="tip", data=tips)
plt.show()

# Gráfico de pares para explorar relacionamentos entre todas as variáveis numéricas.
# A coloração é baseada no sexo ("sex") e usa a paleta "dark".
sns.pairplot(tips, hue="sex", palette="dark")
plt.show()

# Rug plot para a variável "total_bill".
# Mostra marcações na base do eixo que indicam onde os valores estão localizados.
sns.rugplot(tips["total_bill"])
plt.show()

# Criação de um dataset aleatório com 25 valores de distribuição normal.
dataset = np.random.randn(25)

# Rug plot para visualizar a distribuição dos pontos no dataset.
sns.rugplot(dataset)

# Calcula os limites do eixo x para incluir os dados com uma margem extra.
x_min = dataset.min() - 2
x_max = dataset.max() + 2

# Criação de um eixo x contínuo com 100 pontos no intervalo definido.
x_axis = np.linspace(x_min, x_max, 100)

# URL com informações sobre a estimativa de densidade kernel (KDE).
url = "http://en.wikipedia.org/wiki/Kernel_density_estimation#Practical_estimation_of_the_bandwidth"

# Calcula a largura de banda (bandwidth) para a KDE usando uma fórmula padrão.
bandwidth = ((4 * dataset.std() ** 5) / (3 * len(dataset))) ** 0.2

# Lista para armazenar as funções kernel individuais.
kernel_list = []

# Para cada ponto no dataset, cria uma função kernel baseada na distribuição normal.
for data_point in dataset:
    # Criação da função kernel centrada no ponto atual.
    kernel = stats.norm(data_point, bandwidth).pdf(x_axis)
    kernel_list.append(kernel)

    # Normaliza a função kernel para que o pico seja 0.4 na visualização.
    kernel = kernel / kernel.max()
    kernel = kernel * 0.4

    # Plota cada kernel individual com cor cinza e transparência.
    plt.plot(x_axis, kernel, color="grey", alpha=0.5)

# Define o limite superior do eixo y para melhorar a visualização.
plt.ylim(0, 1)
plt.show()

# Soma todas as funções kernel para criar a estimativa de densidade total.
sum_of_kde = np.sum(kernel_list, axis=0)

# Plota a soma das funções kernel (a KDE final).
fig = plt.plot(x_axis, sum_of_kde, color="indianred")

# Adiciona o rug plot para indicar os dados originais na base do gráfico.
sns.rugplot(dataset, c="indianred")

# Remove os rótulos do eixo y para uma visualização mais limpa.
plt.yticks([])

# Adiciona um título ao gráfico.
plt.suptitle("Sum of the Basis Functions")
plt.show()
