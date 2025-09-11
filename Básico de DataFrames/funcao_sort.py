import pandas as pd

# SORT_VALUES()
df = pd.DataFrame({
    "name": ["Mark", "John", "Tim", "Jenny"],
    "age": [55, 33, 41, 12],
    "score": [4.5, 6.7, 3.9, 9.0]
})

print(df.sort_values(by="age"))
print("===" * 20)

"""
Parâmetros últeis

º by → coluna(s) a usar.
º ascending → True (crescente, padrão) ou False (decrescente).
º inplace → True para alterar o DataFrame original.

"""
print(df.sort_values(by=["score", "age"], ascending=[False, True]))
print("===" * 20)

#########################################################################
# SORT_INDEX()
df2 = df.set_index("name")
print(df2.sort_index())

"""
Parâmetros úteis

axis=0 → ordena pelo índice das linhas (padrão).

axis=1 → ordena pelo índice das colunas.

ascending → ordem crescente (True) ou decrescente (False).

inplace → altera o objeto original.
"""
df2.sort_index(axis=1, ascending=False)