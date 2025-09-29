import numpy as np

"""
Array Numpy

Array 1d
array1 = np.array([10, 100, 1000])

Array Bidimensional
array2 = np.array([1.,2.,3.], 
                  [4., 5., 6.])
"""

array1 = np.array([10, 100, 1000])
array2 = np.array([1.,2.,3.], 
                  [4., 5., 6.])

# Vetorização e Transmissão

# notação matematica com arrays
array2 + 2

# NumPy executa a operação element-wise
array2 * array2

# O numpy amplia o array menor em um array maior para que suas formas se tornem compativeis
array2 * array1

# Transposição (.T)
# A transposição troca linhas por colunas de uma matriz.
A = np.array([[1, 2, 3],
              [4, 5, 6]])

print("Matriz A:")
print(A)
# [[1 2 3]
#  [4 5 6]]

print("\nTransposta de A:")
print(A.T)
# [[1 4]
#  [2 5]
#  [3 6]]

# Funções ufunc

np.sqrt(array2) # raiz quadrada 

# somar números de cada coluna
array2.sum(axis=0) # o argumento axis=0 refere-se ao eixo linhas e axis=1 ao eixo de colunas

print(np.sum(A))        # Soma total
print(np.sum(A, axis=0))  # Soma por colunas -> [110 15 18]
print(np.sum(A, axis=1))  # Soma por linhas -> [6 15 24]

print(np.max(A)) # Máximo
print(np.min(A)) # Mínimo
print(np.mean(A)) # Média, caso queira a as linhas (axis=0) out colunas (axis=1)
print(np.std(A)) # Desvio paadrão


# Fatiamento de Arrays Bidimensionais
# pegando elementos especificos
print(A[1, 2]) # (Linha 1, Coluna 2)

# pegando linha inteira 
print(A[0, :])

# pegando coluna inteira 
print(A[:, 1])

# Submatriz
print(A[0:2, 1:3])
# [[2 3]
#  [5 6]]

# Construtores de Array Úteis
# arange: retorna um array Numpy
# reshape: gera um array com as dimensões desejadas

np.arange(2 * 5).reshape(2, 5) # 2 linhas, 5 colunas

# Arrays especiais 
np.zeros((2, 3)) # Matriz só com zeros
np.ones((3, 3)) # Matriz só com 1
print(np.eye(3)) # Matriz identidade 3x3
np.arange(0,10,2)    # [0 2 4 6 8]
np.linspace(0,1,5)   # [0.   0.25 0.5  0.75 1.]


# Propriedades mais usadas
x = np.array([[1,2,3],[4,5,6]])

print(x.ndim)   # número de dimensões (2)
print(x.shape)  # formato (linhas, colunas) → (2, 3)
print(x.size)   # total de elementos → 6
print(x.dtype)  # tipo dos dados → int64 ou float64