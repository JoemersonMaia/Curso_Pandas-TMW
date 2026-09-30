# %%
## Leia o arquivo transacoes.csv com a formatação correta;

import pandas as pd

df = pd.read_csv("../../data/transacoes.csv", sep = ";")
df

# %%
## Adicione uma coluna com valores 1;

df["frag"] = 1
df

# %%
##Salve o dataframe com nome: transacoes_1.csv