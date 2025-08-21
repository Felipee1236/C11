import numpy as np

arr1 = np.ones(8, dtype=int)
arr2 = np.random.randint(0, 10, 8)

resultado = arr1 + arr2
print("Array 1:", arr1)
print("Array 2:", arr2)
print("Resultado:", resultado)

soma_total = np.sum(resultado)
print("Soma total:", soma_total)

if soma_total >= 40:
    matriz = resultado.reshape(4, 2)
else:
    matriz = resultado.reshape(2, 4)

print("Matriz final:\n", matriz)
