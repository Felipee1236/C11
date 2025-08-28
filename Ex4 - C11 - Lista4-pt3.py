import numpy as np

ds = np.loadtxt("space.csv", delimiter=";", dtype=str, encoding="utf-8")
colunas = [c.strip() for c in ds[0]]
idx_empresa = colunas.index("Company Name")
idx_custo = colunas.index("Cost")

empresas = np.char.strip(ds[1:, idx_empresa])
custos = np.char.strip(ds[1:, idx_custo]).astype(float)

valores, indices = np.unique(empresas, return_inverse=True)
soma_custos = np.zeros(valores.shape)
np.add.at(soma_custos, indices, custos)

idx_max = np.argmax(soma_custos)
empresa_maior_gasto = valores[idx_max]
valor_maior_gasto = soma_custos[idx_max]

print(f"Empresa que mais gastou: {empresa_maior_gasto} ({valor_maior_gasto:.2f} milhões)")