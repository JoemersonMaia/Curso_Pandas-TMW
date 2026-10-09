# %%

import pandas as pd

df = pd.read_csv("dados_cartao.csv", sep = ";")

df["dtTransacao"] = pd.to_datetime(df["dtTransacao"])

df["vlParcela"] = df["vlVenda"] / df["qtParcelas"]

# %%

df["ordemparcela"] = df.apply(lambda row:[i for i in range(row["qtParcelas"])], axis = 1)
df 

# %% 

df_explode = df.explode("ordemparcela")
df_explode

# %%
def calDtParcela(row):
    dt = row["dtTransacao"] + pd.DateOffset(months=row["ordemparcela"])
    dt =  f"{dt.year}-{dt.month}"
    return dt


df_explode["dtParcela"] = df_explode.apply(calDtParcela, axis=1)
df_explode

# %%

(df_explode.groupby(["idCliente", "dtParcela"])
                    ["vlParcela"].sum()
                    .reset_index()
                    .pivot_table(index='idCliente',
                        columns='dtParcela',
                        values='vlParcela',
                        fill_value=0))
