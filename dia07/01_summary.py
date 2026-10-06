# %%

import pandas as pd

idades = [32,45,55,66,32,30,40,50]
idades = pd.Series(idades)
idades.sum()
idades.min()
idades.max()
idades.mean()
idades.describe()

# %%

clientes = pd.read_csv("../data/clientes.csv", sep = ";")
clientes

# %%

clientes["flTwitch"].sum()
clientes["flTwitch"].mean()

# %%

rede_sociais = ["flEmail","flTwitch","flYouTube","flBlueSky","flInstagram"]
clientes[rede_sociais].describe()


# %%

num_columns = clientes.dtypes[~(clientes.dtypes == "object")].index.tolist()

clientes[num_columns].mean()
# %%

clientes[num_columns].describe()

# %%
