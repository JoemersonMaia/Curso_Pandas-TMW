# %%

import pandas as pd

idades = [110,20,30,40,50,50,60,50,40]
indexs = ["jo", "maria", "silvia", "maria", "joao", "flavia", "margo", "flavia", "socorro"]

series_idades = pd.Series(idades)
series_idades

# %%
idades[0]
series_idades[0]

# %%
series_idades.iloc[-1]
series_idades.iloc[:3]

 # %%
idades = [110,20,30,40,50,50,60,50,40]
indexs = ["jo", "jo", "silvia", "maria", "joao", "flavia", "margo", "flavia", "socorro",]

series_idades = pd.Series(idades, index = indexs)
series_idades

# %%
series_idades["jo"]
series_idades.iloc[-1]
