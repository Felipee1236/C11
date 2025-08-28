import pandas as pd

df = pd.read_csv("space.csv", delimiter=";")
df.columns = [c.strip() for c in df.columns]

empresa_mais_missoes = df["Company Name"].value_counts().idxmax()
qtd_missoes = df["Company Name"].value_counts().max()

print(f"Empresa com mais missões: {empresa_mais_missoes} ({qtd_missoes} missões)")
