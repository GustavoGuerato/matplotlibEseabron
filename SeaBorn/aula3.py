import seaborn as sns  # Biblioteca para visualização de dados
import matplotlib.pyplot as plt  # Biblioteca para criar gráficos

# Carrega o dataset "tips" (informações sobre gorjetas em restaurantes)
# Inclui variáveis como valor total da conta, gorjeta, gênero, e outros detalhes
tips = sns.load_dataset("tips")

# Carrega o dataset "flights" (informações sobre número de passageiros de voos por mês/ano)
# Inclui variáveis como mês, ano e quantidade de passageiros
flights = sns.load_dataset("flights")

# Exibe as 5 primeiras linhas do dataset "tips" para ter uma visão geral das colunas e dados
print(tips.head())

# Exibe as 5 primeiras linhas do dataset "flights" para entender a estrutura e os dados presentes
print(flights.head())

# ------------------------------------------
# MATRIZ DE CORRELAÇÃO PARA O DATASET "TIPS"
# ------------------------------------------

# Seleciona apenas as colunas numéricas do dataset "tips" para calcular a matriz de correlação
# Isso é necessário porque a função corr() só funciona com dados numéricos
tc = tips.select_dtypes(include=["float64", "int64"]).corr()

# Exibe a matriz de correlação no console para análise textual
# A matriz mostra como as variáveis numéricas estão relacionadas entre si
# Por exemplo, valores próximos a 1 indicam alta correlação positiva, e próximos a -1 indicam alta correlação negativa
print(tc)

# Cria um heatmap para visualizar graficamente a matriz de correlação
# O heatmap utiliza a paleta de cores "coolwarm", onde azul indica correlação negativa e vermelho indica positiva
sns.heatmap(tc, annot=True, cmap="coolwarm")

# Adiciona um título ao gráfico para melhor entendimento
plt.title("Heatmap da Matriz de Correlação (Tips Dataset)")

# Exibe o heatmap na tela
plt.show()

# ------------------------------------------
# HEATMAP PARA O DATASET "FLIGHTS"
# ------------------------------------------

# Cria uma tabela dinâmica (pivot table) do dataset "flights"
# A tabela tem os meses como índices (linhas), os anos como colunas, e os valores de passageiros como conteúdo
# O parâmetro `observed=False` mantém o comportamento atual, considerando todas as combinações possíveis
fp = flights.pivot_table(
    index="month",  # Define os meses como índices (linhas)
    columns="year",  # Define os anos como colunas
    values="passengers",  # Os valores da tabela são o número de passageiros
    observed=False,  # Mantém o comportamento atual para variáveis categóricas
)

# Cria um heatmap para visualizar os dados da tabela dinâmica de "flights"
# Cada célula representa o número de passageiros para um mês/ano específico
sns.heatmap(fp, cmap="YlGnBu", annot=False)

# Adiciona um título ao gráfico para descrever o que ele representa
plt.title("Heatmap do Dataset Flights")

# Exibe o heatmap na tela
plt.show()

# ------------------------------------------
# CLUSTER MAP PARA O DATASET "FLIGHTS"
# ------------------------------------------

# Cria um cluster map para visualizar os padrões e agrupar dados similares
# O cluster map utiliza um algoritmo de agrupamento hierárquico para organizar os dados
# O parâmetro `standard_scale=1` normaliza os dados por coluna (anos), ou seja, padroniza os valores para melhor comparação
sns.clustermap(fp, standard_scale=1, cmap="coolwarm")

# Exibe o cluster map na tela
# O cluster map agrupa os meses e anos com padrões semelhantes, facilitando a análise de tendências
plt.title("Cluster Map do Dataset Flights")
plt.show()
