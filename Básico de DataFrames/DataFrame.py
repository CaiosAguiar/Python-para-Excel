import pandas as pd

#read_excel retorna um DataFrame
df = pd.read_excel(r"C:\Users\caios\OneDrive\Desktop\Python para Excel\Cápitulo 5\Planilhas\course_participants.xlsx")

# criar dataframes com arrays
data = [["Mark", 55, "Italy", 4.5, "Europe"],
        ["John", 33, "USA", 6.7, "America"],
        ["Tim", 41, "USA", 3.9, "America"],
        ["Jenny", 12, "Germany", 9.0, "Europe"]]

# (parâmentro da função) data=data (nome da variável)
df = pd.DataFrame(data=data,
                  columns=["name", "age", "country",
                           "score", "continent"],
                  index=[1001, 1000, 1002, 1003])
df
# mostra infomação do DataFrame
df.info()
# mostra tipos de dados da coluna
print(df.dtypes)
# dar nome ao um índice
df.index.name = "user_id"
print(df)
print("==" * 20)
# para transformar o índice em um coluna, use (reset_index) 
df.reset_index() # isso é temporario 
print(df)
# df = df.reset_index() # isso não
print("==" * 20)
# (set_index) transforma coluna em índice
df1 = df.reset_index().set_index("name")
print(df1)

print("==" * 20)
# para alterar o índice, use o método reindex
df = df.reindex([999, 1000, 1001, 1004])
print(df)