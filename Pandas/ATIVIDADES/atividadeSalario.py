import pandas as pd

# Carrega o arquivo CSV "Salaries.csv" em um DataFrame do Pandas
df = pd.read_csv("Salaries.csv")

# Substitui os valores ausentes (NaN) por 0 no DataFrame. Isso é útil para evitar erros em cálculos.
df.fillna(0, inplace=True)

# Exibe as primeiras 5 linhas do DataFrame, ajudando a verificar rapidamente como os dados estão estruturados
print(df.head())

# Exibe um resumo das colunas do DataFrame, incluindo o tipo de dado de cada coluna e o número de valores não nulos
print(df.info())

# Converte a coluna "BasePay" para o tipo numérico, caso haja valores que não podem ser convertidos, como strings,
# o parâmetro "errors='coerce'" forçará esses valores a se tornarem NaN.
df["BasePay"] = pd.to_numeric(df["BasePay"], errors="coerce")

# Realiza a mesma conversão para a coluna "OvertimePay"
df["OvertimePay"] = pd.to_numeric(df["OvertimePay"], errors="coerce")

# Calcula a média da coluna "BasePay", que é a soma de todos os valores dividida pelo número de registros.
avg_basepay = df["BasePay"].mean()

# Encontra o maior valor presente na coluna "OvertimePay", indicando o maior pagamento de horas extras
highest_overpay = df["OvertimePay"].max()

# Encontra a linha com o maior valor na coluna "TotalPayBenefits", que é o salário total somado aos benefícios
# A função idxmax() retorna o índice da linha que contém o maior valor da coluna especificada.
highest_salary = df.loc[df["TotalPayBenefits"].idxmax()]

# Encontra a linha com o menor valor em "TotalPayBenefits" (o salário total + benefícios mais baixos)
lowest_salary = df.loc[df["TotalPayBenefits"].idxmin()]

# Filtra o DataFrame para encontrar as informações do funcionário chamado "JOSEPH DRISCOLL"
# Esse filtro vai retornar todas as linhas que possuem esse nome na coluna "EmployeeName"
joseph_row = df[df["EmployeeName"] == "JOSEPH DRISCOLL"]

# Extrai o título do cargo de Joseph Driscoll a partir da linha filtrada, pegando o valor da coluna "JobTitle"
job_title = joseph_row["JobTitle"].values[0]

# Obtém os 5 cargos mais comuns no DataFrame usando a função "value_counts()", que conta as ocorrências de cada título de cargo
top_five_job = df["JobTitle"].value_counts().head(5)

# Calcula o pagamento anual de Joseph Driscoll, somando as colunas de BasePay, OvertimePay, OtherPay e Benefits
# O valor é extraído diretamente da linha do DataFrame filtrado para Joseph Driscoll
anual_pay = (
    joseph_row["BasePay"].values[0]
    + joseph_row["OvertimePay"].values[0]
    + joseph_row["OtherPay"].values[0]
)

# Acrescenta o valor de Benefits ao pagamento anual de Joseph Driscoll
anual_pay += joseph_row["Benefits"].values[0]

# Filtra o DataFrame para considerar apenas os registros de 2011 a 2014 (usando o operador lógico & para combinar condições)
filtered_years = df[(df["Year"] >= 2011) & (df["Year"] <= 2014)]

# Agrupa os dados por "Year" e calcula a soma de "BasePay" por ano. O método "sum" vai somar os valores de BasePay para cada ano.
avg_BasePay_years = filtered_years.groupby("Year")["BasePay"].sum()

# Conta o número de títulos de cargos únicos no DataFrame (sem repetir os mesmos cargos)
job_Title_Unique = df["JobTitle"].nunique()

# Filtra os dados de 2013 e conta a quantidade de títulos de cargos distintos que aparecem no ano de 2013
unique_job_titles = df[df["Year"] == 2013]["JobTitle"].value_counts()

# Conta quantos cargos aparecem apenas uma vez em 2013 (valor igual a 1 na contagem de cada cargo)
single_job_titles_count = (unique_job_titles == 1).sum()

# Conta quantos cargos contêm a palavra "Chief" (ignorando maiúsculas e minúsculas, por isso "case=False")
# Isso ajuda a identificar quantos cargos de alto escalão (como Chief Executive Officer) estão presentes.
chief_count = df["JobTitle"].str.contains("Chief", case=False, na=False).sum()

# Cria uma nova coluna chamada "JobTitleLength", que contém o comprimento (número de caracteres) do título do cargo
# A função apply() aplica uma função lambda a cada valor da coluna "JobTitle"
df["JobTitleLength"] = df["JobTitle"].apply(lambda x: len(str(x)))

# Calcula a correlação entre o comprimento do título do cargo e o salário total + benefícios
# A correlação indica se há uma relação linear entre o comprimento do cargo e o valor de pagamento total (quanto maior o cargo, maior o pagamento?)
correlation = df["JobTitleLength"].corr(df["TotalPayBenefits"])

# Exibe o valor da correlação, que pode variar de -1 (negativa) a 1 (positiva), e 0 indica nenhuma correlação
print(correlation)

# Exibe o número de títulos de cargos únicos no DataFrame
print(job_Title_Unique)

# Exibe a média de "BasePay" (salário base) no DataFrame
print(f"Média de BasePay: {avg_basepay}")

# Exibe o maior valor de "OvertimePay" (pagamento de horas extras)
print(f"Maior valor de OvertimePay: {highest_overpay}")

# Exibe o cargo de Joseph Driscoll, extraído anteriormente
print(f"Cargo de Joseph Driscoll: {job_title}")

# Exibe o pagamento anual de Joseph Driscoll, somado no cálculo anterior
print(f"Pagamento anual de Joseph Driscoll: {anual_pay}")

# Exibe a linha com o maior salário total (salário + benefícios)
print(highest_salary)

# Exibe a linha com o menor salário total (salário + benefícios)
print(lowest_salary)

# Exibe a soma de BasePay por ano (entre 2011 e 2014) para analisar a evolução do salário
print(avg_BasePay_years)

# Exibe os 5 cargos mais comuns
print(top_five_job)

# Exibe o número de cargos únicos que aparecem apenas uma vez no ano de 2013
print(single_job_titles_count)
