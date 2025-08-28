import pandas as pd

df = pd.read_csv("space.csv", delimiter=";")
df.columns = [c.strip() for c in df.columns]

df["Cost"] = pd.to_numeric(df["Cost"], errors="coerce")
empresa_maior_gasto = df.groupby("Company Name")["Cost"].sum().idxmax()
valor_maior_gasto = df.groupby("Company Name")["Cost"].sum().max()

print(f"Empresa que mais gastou: {empresa_maior_gasto} ({valor_maior_gasto:.2f} milhões)")
