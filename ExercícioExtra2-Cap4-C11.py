import numpy as np

ds = np.loadtxt('paises.csv', delimiter=';', dtype=str, encoding='utf-8-sig')

colunas = [c.strip() for c in ds[0]]
idx_region = colunas.index("Region")
regioes = np.char.strip(ds[1:, idx_region])
mascara_north_america = (regioes == "NORTHERN AMERICA")
qtd_paises = np.sum(mascara_north_america)

print(f"Quantidade de países na América do Norte: {qtd_paises}")