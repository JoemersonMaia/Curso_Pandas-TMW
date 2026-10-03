##05.01 - Crie uma coluna nova “twitch_points” que e resultado da multiplicação do saldo 
# de pontos e a marcação da twitch
##05.02 - Aplique o log na coluna de saldo de pontos, criando uma coluna nova
##05.03 - Crie uma coluna que sinalize se a pessoa tem vínculo com alguma (qualquer uma) 
# plataforma de rede social.
##05.04 - Qual é o id de cliente que tem maior saldo de pontos? E o menor?
##05.05 - Selecione a primeira transação diária de cada cliente.
# %%
## 05.01









# %%
 
import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv", sep = ";")
transacoes.head()

transacoes["data"] = pd.to_datetime(transacoes["DtCriacao"]).dt.date
transacoes = transacoes.sort_values("DtCriacao")

# %%

first = (transacoes.drop_duplicates(keep = "first", subset = ["IdCliente", "data"]))

last = (transacoes.drop_duplicates(keep = "last", subset = ["IdCliente", "data"]))

pd.concat([last, first])