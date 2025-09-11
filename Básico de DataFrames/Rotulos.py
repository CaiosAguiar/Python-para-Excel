import pandas as pd

#df = pd.read_excel(r"C:\Users\caios\OneDrive\Desktop\Python para Excel\Cápitulo 5\Planilhas\course_participants.xlsx")


data = [["Mark", 55, "Italy", 4.5, "Europe"],
        ["John", 33, "USA", 6.7, "America"],
        ["Tim", 41, "USA", 3.9, "America"],
        ["Jenny", 12, "Germany", 9.0, "Europe"]]

df = pd.DataFrame(data=data,
                  columns=["name", "age", "country",
                           "score", "continent"],
                  index=[1001, 1000, 1002, 1003])
df

# reordenar colunas com .loc[: ["colunas reodenadas..."]]
# : → seleciona todas as linhas.
# [ ... ] → define a ordem das colunas explicitamente.
colunas_reordenadas = df.loc[:,[ "continent", "country", "name", "age", "score"]]
print(colunas_reordenadas)

# Use o loc, que siginifica localização, para linhas e colunas que você deseja pegar
# df.loc[row.section, column_section]

# Valor Único / Tipo de dado retornado: escalar
# tabela_pais = (df.loc[1000, "country"])
# print(tabela_pais)

# Uma coluna (1d) / Série
print(df.loc[: , "country"])
print("=" * 20)

# Uma coluna (2d) - bidimensional / DataFrame
print(df.loc[:, ["country"]])  # a difença de uma coluna (2d) e (1d) é o retorno delas 2d = um DataFrame uma tabela comum e uma coluna 1d = parecido com um dicianário em python, tem apenas uma coluna

