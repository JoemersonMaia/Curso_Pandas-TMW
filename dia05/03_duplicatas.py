# %%

import pandas as pd

# %%

df = pd.DataFrame({
    "nome" : ['teo','maria', 'margo', 'margo', 'margo'],
    "sobrenome" : ['calvo', 'madalena', 'silva', 'silva', 'silva'],
    "salario" : [2132,4000,500,6000,300]
})
    
df

# %%
df = df.sort_values("salario", ascending = False)
df

#%%
df = (df.sort_values("salario", ascending = False)
    .drop_duplicates(keep = 'last', subset = ["nome", "sobrenome"]))

df