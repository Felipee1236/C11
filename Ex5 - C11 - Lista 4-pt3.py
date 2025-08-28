import pandas as pd

df = pd.read_csv("space.csv", delimiter=";")
df.columns = [c.strip() for c in df.columns]

ano = df["Datum"].str[-4:]
df["Ano"] = ano
mais_lancamentos = df["Ano"].value_counts().idxmax()
qtd_lancamentos = df["Ano"].value_counts().max()

print(f"Ano com mais lançamentos: {mais_lancamentos} ({qtd_lancamentos} lançamentos)")
