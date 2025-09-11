import pandas as pd

df = pd.read_excel(r"C:\Users\caios\OneDrive\Desktop\Python para Excel\Cápitulo 5\Planilhas\course_participants.xlsx")

data = [["Mark", 55, "Italy", 4.5, "Europe"],
        ["John", 33, "USA", 6.7, "America"],
        ["Tim", 41, "USA", 3.9, "America"],
        ["Jenny", 12, "Germany", 9.0, "Europe"]]

df = pd.DataFrame(data=data,
                  columns=["name", "age", "country",
                           "score", "continent"],
                  index=[1001, 1000, 1002, 1003])
df

# Criar um nome para o índice
df.index.name = "user_id"
# índice vira coluna
df.reset_index()

# para obter informações sobre as colunas de um DataFrame
print(df.columns)
print("==" * 40) 

# nomear colunas df.columns.name = "nome_coluna"
df1 = df.columns.name = "properties"
print(df1)
print("==" * 40)

# renomear colunas df.rename(columns={"nome antigo": "novo nome"})
print(df.rename(columns={"name": "First Name", "age": "Age"}))

"""
para excluir colunas e índices use df.drop(columns["nome coluna"], index=[índices...])
PARA LEMBRAR !!! 
para renomer colunas use columns={chaves}
para excluir colunas use columns=[colchetes]
as colunas e o índice de um DataFrame são representados por um objeto INDEX 

""" 
# excluindo colunas e índices
df_deletando_coisas = df.drop(columns=["name", "country"],
                              index=[1000, 1003])
print(df_deletando_coisas)
print("==" * 40)

# transformar colunas em índices com .transpose()
trocando_objetos = df.transpose()
print(trocando_objetos)
print("==" * 40)

