import numpy as np
import pandas as pd
from sqlalchemy import create_engine

# Lê um arquivo CSV e exibe o conteúdo
print(pd.read_csv("data.csv"))  # Carrega e imprime os dados do arquivo "data.csv"

# Lê o mesmo CSV e armazena em um DataFrame
df = pd.read_csv("data.csv")  # Armazena os dados do CSV em um DataFrame chamado 'df'

# Salva o DataFrame em um novo arquivo CSV
df.to_csv("My_Output.csv", index=False)
# Cria um arquivo chamado "My_Output.csv" com os dados, excluindo o índice

# Lê um arquivo Excel especificando a planilha
pd.read_excel("data.xlsx", sheet_name="Planilha1")
# Lê dados da planilha chamada "Planilha1" no arquivo "data.xlsx"

# Salva o DataFrame em um arquivo Excel
df.to_excel("excel_Sample.xlsx")
# Cria um arquivo Excel chamado "excel_Sample.xlsx" com os dados do DataFrame

# Lê tabelas HTML de um site e armazena como uma lista de DataFrames
data = pd.read_html("https://www.fdic.gov/bank-failures/failed-bank-list")
# Lê todas as tabelas HTML da página fornecida (útil para capturar tabelas diretamente de websites)

# Exibe a primeira tabela extraída da página
print(data[0])
# 'data' é uma lista de DataFrames. Aqui, estamos imprimindo a primeira tabela extraída

# Cria um banco de dados SQLite na memória
engine = create_engine("sqlite:///:memory:")
# Cria uma conexão SQLite temporária (o banco de dados será armazenado na memória)

# Salva o DataFrame 'df' como uma tabela SQL chamada "my_table"
df.to_sql("my_table", engine)
# Converte o DataFrame em uma tabela chamada "my_table" no banco de dados SQLite

# Executa uma consulta SQL para ler a tabela "my_table" e armazena o resultado em um DataFrame
sqldf = pd.read_sql("my_table", con=engine)
# Lê os dados da tabela "my_table" do SQLite e os converte novamente em um DataFrame

# 'sqldf' agora contém os dados recuperados do banco de dados SQL
