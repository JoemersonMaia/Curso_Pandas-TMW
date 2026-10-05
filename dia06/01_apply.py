# %%

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep = ";")
clientes.head()

# %%

idCliente = "001ebba5-5491-400a-ad05-d9204ea11cca"

def get_last_id(x):
    return x.split("-")[-1]

# %%

get_last_id("0019bb9e-26d4-4ebf-8727-fc911ea28a92")

# %%
id_novo = []
for i in clientes["idCliente"]:
    novo = get_last_id(i)
    id_novo.append(novo)

clientes["novo_id"] = id_novo
clientes.head()

# %%

clientes["idCliente"].apply(get_last_id)
