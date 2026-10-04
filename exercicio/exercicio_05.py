##05.01 - Crie uma coluna nova “twitch_points” que e resultado da 
# multiplicação do saldo de pontos e a marcação da twitch
##05.02 - Aplique o log na coluna de saldo de pontos, criando uma coluna nova
##05.03 - Crie uma coluna que sinalize se a pessoa tem vínculo 
# com alguma (qualquer uma)  plataforma de rede social.
##05.04 - Qual é o id de cliente que tem maior saldo de pontos? E o menor?
##05.05 - Selecione a primeira transação diária de cada cliente.
# %%
import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep = ";")

clientes["twitch_points"] = clientes["flTwitch"] * clientes["qtdePontos"]

clientes

# %%
import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep = ";")
filtro = (clientes["flTwitch"] == 1) | (clientes["flYouTube"] == 1) | (clientes["flBlueSky"] == 1) | (clientes["flInstagram"] == 1) 
clientes[filtro]
clientes["vi_social"] = 1
clientes

# %%

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep = ";")

clientes.sort_values(by = ["qtdePontos"], ascending=True).head(1)

# %%
import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv", sep = ";")
transacoes.sort_values(by = ["DtCriacao", "IdCliente"])
filtro_id = transacoes["IdCliente"] == 'a327611d-a675-4f90-bce8-5aef803458a8'
transacoes[filtro_id]

# %%

## 05.08 — Selecione os 5 clientes com maior saldo de pontos.

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep = ";")
clientes.sort_values(by = "qtdePontos", ascending = False).head(5)

# %%

## 05.09 — Selecione os 5 clientes com menor saldo de pontos.


import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep = ";")
clientes.sort_values(by = "qtdePontos", ascending = True).head(5)

# %%

##05.10 — Selecione todas as transações de um determinado cliente e 
# ordene pela data da transação, da mais antiga para a mais recente.

import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv", sep = ";")
filtro_id =transacoes["IdCliente"] == "24782f0b-4683-4f35-976a-ea21d6714ba6"
transacoes[filtro_id].sort_values( by = "DtCriacao")

# %%
## 05.11 — Ordene as transações pela data de criação, da mais 
# antiga para a mais recente, e selecione as 10 primeiras transações.

import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv", sep =";")
transacoes.sort_values(by = "DtCriacao", ascending=False).head(10)

# %%
##05.13 — Selecione todas as transações realizadas por um cliente específico
#  e mostre apenas as 5 primeiras.

import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv", sep = ";")
filtro_id = transacoes["IdCliente"] == "24782f0b-4683-4f35-976a-ea21d6714ba6"
transacoes.sort_values(by = "DtCriacao").head(5)

# %%
##05.16 — Selecione a primeira transação de cada cliente,
#  considerando a transação com a menor DtCriacao.

import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv", sep = ";")
transacoes.sort_values(by = "DtCriacao")