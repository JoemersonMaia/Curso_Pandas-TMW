##04.01 - Quantos clientes tem vínculo com a Twitch?
##04.02 - Quantos clientes tem um saldo de pontos maior que 1000?
##04.03 - Quantas transações ocorreram no dia 2025-02-01?

# %%

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep = ";")

# %%
filtroTwitch = clientes["flTwitch"] == 1
clientes[filtroTwitch]

clientes[filtroTwitch].shape

# %%

filtro_Pontos = clientes["qtdePontos"] > 1000
clientes[filtro_Pontos]

clientes[filtro_Pontos].shape


# %%
transacoes = pd.read_csv("../data/transacoes.csv", sep = ";")

transacoes["DtCriacao"] = pd.to_datetime(transacoes["DtCriacao"])
transacoes["DtCriacao"] = transacoes["DtCriacao"].dt.date
filtro_data = transacoes["DtCriacao"] == pd.to_datetime("2025-09-17").date()

transacoes[filtro_data]