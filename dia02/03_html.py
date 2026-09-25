# %%

import pandas as pd

url = "https://oobj.com.br/bc/quais-codigos-uf-brasil/"
dfs = pd.read_html(url)
dfs

# %%
df_uf = dfs[0]
df_uf.to_csv("ufs.csv", sep =";", index = False) 