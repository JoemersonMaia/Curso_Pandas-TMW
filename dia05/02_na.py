# %%

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep = ";")
clientes

 # %%

clientes = clientes.dropna(how = "all", subset=["qtdePontos"])
clientes = clientes.dropna(how = "any", subset=["qtdePontos", "DtCriacao"])

clientes

# %%

clientes["idade"].fillna(0)

# %%

clientes.fillna({"nome" : "alguem", "idade" : 0})

