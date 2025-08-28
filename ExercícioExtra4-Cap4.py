import numpy as np

ds = np.loadtxt('paises.csv', delimiter=';', dtype=str, encoding='utf-8-sig')
colunas = [c.strip() for c in ds[0]]
idx_region = colunas.index("Region")

regioes = np.char.strip(ds[1:, idx_region])
valores, contagens = np.unique(regioes == "North America", return_counts=True)

print("Regiões e quantidade de países:")
for regiao, qtd in zip(valores, contagens):
    print(f"{regiao}: {qtd}")