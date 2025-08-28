import numpy as np


ds = np.loadtxt("space.csv", delimiter=";", dtype=str, encoding="utf-8")

colunas = [c.strip() for c in ds[0]]


idx_status = colunas.index("Status Mission")

status_missoes = np.char.strip(ds[1:, idx_status])

missoes_sucesso = np.sum(status_missoes == "Success")

total_missoes = status_missoes.size

percentual_sucesso = (missoes_sucesso / total_missoes) * 100

print(f"Percentual de missões bem-sucedidas: {percentual_sucesso:.2f}%")