import numpy as np
import pandas as pd

# Criando um dicionário com dados fictícios
data = {
    "Company": ["GOOG", "GOOG", "MSFT", "MSFT", "FB", "FB"],  # Nome das empresas
    "Person": ["Sam", "Charlie", "Amy", "Vanessa", "Carl", "Sarah"],  # Nome das pessoas
    "Sales": [200, 120, 340, 124, 243, 350],  # Vendas de cada pessoa
}

# Convertendo o dicionário em um DataFrame
df = pd.DataFrame(data)

# Agrupando o DataFrame pela coluna "Company"
# A função .groupby() cria um agrupamento baseado na coluna fornecida (neste caso, 'Company')
# Em seguida, usamos a função .sum() para somar os valores das colunas numéricas dentro de cada grupo
ByCompany = df.groupby("Company").sum()

# Exibindo o resultado
print(ByCompany)

# Saída esperada:
# A coluna "Sales" será somada para cada empresa (GOOG, MSFT, FB).
# A coluna "Person" não será afetada pela função sum(), pois contém dados de texto e não pode ser somada.
