# %%

import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep = ";")
df.head()

# %%
filtro = df["QtdePontos"] > 50

df[filtro]

# %%
filtro = df["QtdePontos"] >= 50 

df[filtro]

# %%

filtro = (df["QtdePontos"] >= 50) * (df["QtdePontos"] <= 100)
df[filtro]

# %%
filtro = (df["QtdePontos"] == 1) | (df["QtdePontos"] == 100)
df[filtro]

# %%
filtro = (df["QtdePontos"] > 0) & ((df["QtdePontos"] <= 50) | (df["DtCriacao"] > '2025-09-17'))
df[filtro]