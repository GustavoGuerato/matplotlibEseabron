import pandas as pd

# Carrega o arquivo CSV para dentro de um DataFrame.
# O DataFrame 'df' agora contém todos os dados do arquivo "EcommercePurchases.csv"
df = pd.read_csv("EcommercePurchases.csv")

# Substitui os valores ausentes (NaN) por 0
# Isso garante que não haja valores ausentes no DataFrame, substituindo por 0 onde necessário.
df.fillna(0, inplace=True)

# Exibe as primeiras 5 linhas do DataFrame para uma visão geral inicial.
# A função 'head()' mostra uma amostra dos dados para visualização.
print(df.head())

# Exibe informações gerais sobre o DataFrame, como o tipo de cada coluna e o número de valores não nulos.
# A função 'info()' ajuda a entender rapidamente a estrutura do DataFrame.
print(df.info())

# Calcula e imprime a média da coluna 'Purchase Price', que representa os preços das compras.
# A função 'mean()' retorna a média dos valores numéricos dessa coluna.
print(df["Purchase Price"].mean())

# Encontra o maior preço na coluna 'Purchase Price', ou seja, o valor máximo.
# 'max()' retorna o maior valor de uma coluna numérica.
highest_price = df["Purchase Price"].max()

# Encontra o menor preço na coluna 'Purchase Price', ou seja, o valor mínimo.
# 'min()' retorna o menor valor de uma coluna numérica.
lowest_price = df["Purchase Price"].min()

# Imprime os maiores e menores preços encontrados
print(highest_price)
print(lowest_price)

# Filtra os dados para mostrar apenas as compras feitas em inglês (onde a coluna 'Language' é igual a 'en')
# Esse filtro seleciona apenas as linhas do DataFrame onde o valor da coluna 'Language' é 'en'.
english_data = df[df["Language"] == "en"]

# Conta o número de valores não nulos em cada coluna do DataFrame filtrado
# 'notnull()' retorna um DataFrame booleano indicando valores não nulos (True), e 'sum()' conta o número de True.
column_counts = english_data.notnull().sum()

# Imprime a contagem de valores não nulos por coluna, formatando a saída
output = "\n".join([f"{column:<20} {count}" for column, count in column_counts.items()])
print(output)

# Filtra os dados para mostrar apenas as linhas onde a coluna 'Job' é igual a 'Lawyer' (advogados).
# Isso seleciona as linhas onde as pessoas são advogados, conforme o campo 'Job'.
lawyers = df[df["Job"] == "Lawyer"]
print(lawyers)

# Conta a quantidade de ocorrências de 'AM' e 'PM' na coluna "AM or PM"
# 'value_counts()' conta as ocorrências de cada valor único na coluna, neste caso, AM ou PM.
counts = df["AM or PM"].value_counts()

# Imprime a contagem de AM ou PM
print(counts)

# Encontra e imprime os 5 empregos mais comuns (top 5) presentes na coluna 'Job'.
# 'value_counts().head(5)' conta as ocorrências de cada valor na coluna 'Job' e retorna os 5 mais frequentes.
top_5_jobs = df["Job"].value_counts().head(5)
print(top_5_jobs)

# Filtra os dados para mostrar o preço de compra das pessoas que têm o "Lot" igual a "90 WT"
# 'loc' é utilizado para filtrar as linhas do DataFrame baseadas em uma condição específica e selecionar apenas a coluna 'Purchase Price'.
purchase_price = df.loc[df["Lot"] == "90 WT", "Purchase Price"]
print(purchase_price)

# Filtra os dados para mostrar o email associado a um número de cartão de crédito específico.
# 'loc' permite filtrar pelo número do cartão e retorna o valor correspondente da coluna 'Email'.
credit_card = df.loc[df["Credit Card"] == 4926535242672853, "Email"]
print(credit_card)

# Filtra os dados para mostrar compras feitas com o provedor de cartão "American Express"
# E também filtra as compras com valor superior ou igual a 95.
provider = df[(df["CC Provider"] == "American Express") & (df["Purchase Price"] >= 95)]
print(provider)

# Filtra os dados para mostrar cartões de crédito que expiram em 2025, verificando os últimos dois caracteres da coluna 'CC Exp Date'.
# 'str[-2:]' pega os dois últimos caracteres da string, que representam o ano de expiração.
expires_data = df[df["CC Exp Date"].str[-2:] == "25"]
print(expires_data)

# Conta os 5 emails mais frequentes no DataFrame e os imprime.
# 'value_counts()' conta as ocorrências de cada email, e 'head(5)' retorna os 5 mais comuns.
top_5_emails = df["Email"].value_counts().head(5)
print(top_5_emails)
