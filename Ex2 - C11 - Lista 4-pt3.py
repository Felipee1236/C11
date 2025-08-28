import pandas as pd

df = pd.read_csv("space.csv", delimiter=";")
df.columns = [c.strip() for c in df.columns]

df["Cost"] = pd.to_numeric(df["Cost"], errors="coerce")
media_gastos = df[df["Cost"] > 0]["Cost"].mean()

print(f"Média de gastos das missões com valores disponíveis: {media_gastos:.2f} milhões")
