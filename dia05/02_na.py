# %%

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep = ";")
clientes

 # %%

clientes = clientes.dropna(how = "all", subset=["qtdepontos"])
clientes = clientes.dropna(how = "any", subset=["qtdepontos", "DtCriacao"])

clientes

# %%

clientes["idade"].fillna(0)

# %%

clientes.fillna({"nome" : "alguem", "idade" : 0})

