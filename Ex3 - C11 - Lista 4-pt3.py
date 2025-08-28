import numpy as np

ds = np.loadtxt("space.csv", delimiter=";", dtype=str, encoding="utf-8")
colunas = [c.strip() for c in ds[0]]
idx_empresa = colunas.index("Company Name")

empresas = ds[1:, idx_empresa]
empresas = np.char.strip(empresas)

valores, contagens = np.unique(empresas, return_counts=True)
idx_max = np.argmax(contagens)
empresa_mais_missoes = valores[idx_max]
qtd_missoes = contagens[idx_max]

print(f"Empresa com mais missões: {empresa_mais_missoes} ({qtd_missoes} missões)")