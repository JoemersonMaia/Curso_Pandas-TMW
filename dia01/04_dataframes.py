# %%
import pandas as pd

idades = [110,20,30,40,50,50,60,50,40]
nomes = ["jo", "maria", "silvia", "maria", "joao", "flavia", "margo", "flavia", "socorro"]

series_idades = pd.Series(idades)
series_nomes = pd.Series(nomes)

# %%

df = pd.DataFrame()
df["idades"] = series_idades
df["nomes"] = series_nomes
df

# %%

df.iloc[0]["nomes"]

# %%

df.iloc[-1]["idades"]