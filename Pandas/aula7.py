import numpy as np
import pandas as pd

# Criação de um DataFrame básico com 3 colunas e 4 linhas
df = pd.DataFrame(
    {
        "col1": [1, 2, 3, 4],  # Números inteiros
        "col2": [444, 555, 666, 444],  # Valores repetidos e únicos
        "col3": ["abc", "def", "ghi", "xyz"],  # Strings
    }
)

# Exibe as 5 primeiras linhas do DataFrame
df.head()  # Muito útil para verificar rapidamente a estrutura e os dados do DataFrame

# Contar o número de valores únicos na coluna 'col2'
df["col2"].nunique()  # Retorna a quantidade de valores únicos presentes em 'col2'

# Contar a frequência de cada valor na coluna 'col2'
df["col2"].value_counts()  # Mostra quantas vezes cada valor aparece

# Filtrar linhas onde col1 > 1 e col2 == 444
df[(df["col1"] > 1) & (df["col2"] == 444)]  # Útil para realizar análises condicionais


# Definir uma função personalizada
def times2(x):
    return x * 2  # A função multiplica o valor de entrada por 2


# Aplicar a função personalizada na coluna 'col1'
df["col1"].apply(times2)  # Multiplica todos os valores de col1 por 2

# Calcular o comprimento de cada string na coluna 'col3'
df["col3"].apply(len)  # Retorna o número de caracteres de cada string

# Usar uma função lambda para multiplicar os valores de 'col2' por 2
df["col2"].apply(lambda x: x * 2)  # Realiza a mesma operação, mas de forma inline

# Remover a coluna 'col1' do DataFrame
df.drop(
    "col1", axis=1
)  # axis=1 significa que estamos removendo colunas (não modifica sem inplace=True)

# Ordenar os valores do DataFrame com base na coluna 'col2'
df.sort_values("col2")  # Retorna um DataFrame ordenado pela coluna 'col2'

# Verificar valores nulos no DataFrame
df.isnull()  # Retorna um DataFrame booleano indicando a presença de valores nulos

# Criação de outro DataFrame para estudo de tabelas dinâmicas
data = {
    "A": ["foo", "foo", "foo", "bar", "bar", "bar"],  # Categorias repetidas
    "B": ["one", "one", "two", "two", "one", "one"],  # Subcategorias
    "C": ["x", "y", "x", "y", "x", "y"],  # Outra coluna categórica
    "D": [1, 3, 2, 5, 4, 1],  # Valores numéricos associados
}

df1 = pd.DataFrame(data)  # Criação de outro DataFrame

print(df1)  # Mostra a estrutura do novo DataFrame

# Criar uma tabela dinâmica com base no DataFrame 'df1'
print(df1.pivot_table(values="D", index=["A", "B"], columns=["C"]))
# Tabela dinâmica (pivot table):
# - 'values="D"': Usa os valores da coluna D
# - 'index=["A", "B"]': Define A e B como índices (linhas)
# - 'columns=["C"]': Os valores únicos de C se tornam colunas
# Útil para análises e reorganização de dados
