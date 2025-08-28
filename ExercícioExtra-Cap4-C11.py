import numpy as np

ds = np.loadtxt('paises.csv', delimiter=';', dtype=str, encoding='utf-8-sig')
colunas = [c.strip() for c in ds[0]]

indices = [colunas.index(c) for c in ["Country", "Region", "Population", "Area (sq. mi.)"]]
for linha in ds[1:, indices]:
    print('; '.join(linha))