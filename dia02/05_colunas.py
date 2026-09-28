# %%

import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep=";")
df

# %%
df.shape

# %%
df.info(memory_usage='deep')

# %%
df.dtypes

#%%
df.rename(columns={
                        "QtdePontos" : "qtPontos",
                        "DescSistemaOrigem" : "SitemaOrigem"}, inplace=True)

# %%
colunas = ["IdCliente", "qtPontos"]
df[colunas] 

# %%
## SELECT * FROMdf
df

# %%
##SELECT IdCliente FROM df
df[["IdCliente"]]

# %%
##SELECT IdCliente, qtPontos FROM df LIMIT 5
df[["IdCliente", "qtPontos"]].tail(5)

# %%

## select IdCLiente, Idtransacao, qtPontos,
## FROM DF
## LIMIT 5

df[["IdCliente", "qtPontos"]].head(1000)

# %%
colunas = list(df.columns)
colunas.sort()
colunas

df = df[colunas]
df