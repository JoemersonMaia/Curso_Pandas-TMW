##04.01 - Quantos clientes tem vínculo com a Twitch?
##04.02 - Quantos clientes tem um saldo de pontos maior 
# que 1000?
##04.03 - Quantas transações ocorreram no dia 2025-02-01?

# %%

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep = ";")
filtro = clientes["flTwitch"] == 1
clientes[filtro]

# %%

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv")
filtro = clientes["qtdePontos"] > 1000
clientes[filtro]