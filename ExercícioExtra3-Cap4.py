import numpy as np

ds = np.loadtxt("paises.csv", delimiter=";", dtype=str, encoding="utf-8")
colunas = [c.strip() for c in ds[0]]
idx_status = colunas.index("Literacy (%)")
literacy_values = ds[1:, idx_status].astype(float)
media_literacy = np.mean(literacy_values)
print(f"Média de alfabetização (%): {media_literacy:.2f}")