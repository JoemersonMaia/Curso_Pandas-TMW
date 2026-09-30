# %%

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep = ";")

# %%

clientes["qtdePontos"].astype(float)

# %%
replace = {"00" : "01"}
clientes["DtCriacao"] = pd.to_datetime(clientes["DtCriacao"].replace(replace))


# %%

clientes["DtCriacao"].dt.date