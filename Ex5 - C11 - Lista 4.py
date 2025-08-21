import numpy as np

np.random.seed(10)
matriz = np.random.randint(1, 51, (4, 4))
print("Matriz:\n", matriz)

medias_linhas = matriz.mean(axis=1)
medias_colunas = matriz.mean(axis=0)

print("Média das linhas:", medias_linhas)
print("Média das colunas:", medias_colunas)

print("Maior média das linhas:", medias_linhas.max())
print("Maior média das colunas:", medias_colunas.max())

valores, contagens = np.unique(matriz, return_counts=True)
repetidos = valores[contagens == 2]

print("Contagem de cada número:", dict(zip(valores, contagens)))
print("Números que aparecem 2 vezes:", repetidos)
