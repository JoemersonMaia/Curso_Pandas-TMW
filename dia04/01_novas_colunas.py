# %%

import pandas as pd
import numpy as np

df = pd.read_csv("../data/clientes.csv", sep = ";")
df.head()

# %%

df["ponts_100"] = df["qtdePontos"] + 100
df

# %%

df["emailTwitch"] = df["flEmail"] + df["flTwitch"] 
df
    
# %%

df["flEmail"] * df["flTwitch"] 

# %%

df["QtdeRedeSociais"] = df["flEmail"] + df["flTwitch"] + df["flYouTube"] + df["flBlueSky"] + df["flInstagram"] 
df 

# %%

df["todas_social"] = df["flEmail"] * df["flTwitch"] * df["flYouTube"] * df["flBlueSky"] * df["flInstagram"] 
df

# %%

df["qtdePontos"].describe()

# %%

df["logPontots"] = np.log(df["qtdePontos"]+ 1)
df["logPontots"].describe()

# %%

import matplotlib.pyplot as plt

plt.hist(df["logPontots"])
plt.grid(True)
plt.show()