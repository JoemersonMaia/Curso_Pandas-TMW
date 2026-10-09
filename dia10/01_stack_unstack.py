# %%

import pandas as pd

df = pd.read_csv("../dia08/homicidios_consolidado.csv", sep = ";")
df.head()

# %%

df = df.set_index(["nome", "período"])
df_stack = df.stack()

# %%

df_stack = df_stack.reset_index()

df_stack.columns = ["nome", "periodo", "metrica", "valor"]

df_stack

# %%

df_unstack = (df_stack.set_index(["nome", "periodo", "metrica"])
         .unstack()
         .reset_index()
         )


df_unstack

# %%

metricas = df_unstack.columns.droplevel(0)[2:].tolist()
df_unstack.columns = ["nome", "periodo"] + metricas
df_unstack

# %%
metricas