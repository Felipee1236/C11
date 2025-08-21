import numpy as np

matriz = np.random.randint(1, 10, (3, 5))
print("Matriz:\n", matriz)

linhas, colunas = matriz.shape
total_elementos = linhas * colunas
print("Total de elementos:", total_elementos)

if total_elementos % 2 == 0:
    print("O vetor resultante teria quantidade PAR de elementos")
else:
    print("O vetor resultante teria quantidade ÍMPAR de elementos")
