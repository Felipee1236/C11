import pandas as pd

df = pd.read_csv("space.csv", delimiter=";")
df.columns = [c.strip() for c in df.columns]

missoes_sucesso = (df["Status Mission"].str.strip() == "Success").sum()
total_missoes = len(df)
percentual_sucesso = (missoes_sucesso / total_missoes) * 100

print(f"Percentual de missões bem-sucedidas: {percentual_sucesso:.2f}%")