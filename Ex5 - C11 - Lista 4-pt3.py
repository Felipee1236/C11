import numpy as np

ds = np.loadtxt("space.csv", delimiter=";", dtype=str, encoding="utf-8")
colunas = [c.strip() for c in ds[0]]
idx_datum = colunas.index("Datum")

datas = np.char.strip(ds[1:, idx_datum])
anos = np.char.strip(datas)[-4:] if datas.size == 1 else np.char.strip(datas).view(np.chararray)[:, -4:]
anos = np.char.strip(datas).astype(str)
anos = np.char.substr(anos, len(anos[0])-4, 4)

valores, contagens = np.unique(anos, return_counts=True)
idx_max = np.argmax(contagens)
ano_mais_lancamentos = valores[idx_max]
qtd_lancamentos = contagens[idx_max]

print(f"Ano com mais lançamentos: {ano_mais_lancamentos} ({qtd_lancamentos} lançamentos)")