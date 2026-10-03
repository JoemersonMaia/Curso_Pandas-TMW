# %%

import pandas as pd

idades = [110,20,30,40,50,50,60,50,40]

series_idades = pd.Series(idades)
series_idades

# %%

media_idades = series_idades.mean()
var_idades = series_idades.var()
summary_idades = series_idades.describe()

summary_idades
var_idades
media_idades