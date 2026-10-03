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

clientes = pd.read_csv("../data/clientes.csv", sep = ";")
filtro = clientes["qtdePontos"] > 1000
clientes[filtro]


# %%

import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv", sep= ";")
transacoes["DtCriacao"] = pd.to_datetime(transacoes["DtCriacao"])
transacoes["DtCriacao"] = transacoes["DtCriacao"].dt.date
filtro_data = transacoes["DtCriacao"] == pd.to_datetime("2025-02-11").date()
transacoes[filtro_data]

## 04.04 - Quantos clientes têm vínculo com o YouTube?

## 04.05 - Quantos clientes têm vínculo com o Instagram?

## 04.06 - Quantos clientes possuem mais de 500 pontos?

## 04.07 - Quantos clientes possuem exatamente 0 pontos?

## 04.08 - Quantos produtos pertencem à categoria "espada"?

## 04.09 - Quantos produtos possuem a categoria "poção"?

## 04.10 - Quantas transações ocorreram no dia 2025-09-17?

## 04.11 - Quantas transações tiveram origem no sistema "twitch"?

## 04.12 - Quantas transações tiveram origem no sistema "youtube"?

## 04.13 - Quantos registros existem na tabela transacao_produto
##         onde QtdeProduto é igual a 1?

# %%
## 04.04 - Quantos clientes têm vínculo com o YouTube?
import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep = ";")
filtro_yt = clientes["flYouTube"] == 1
clientes[filtro_yt]


# %%
## 04.05 - Quantos clientes têm vínculo com o Instagram?

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep = ";")
filtro_ins = clientes["flInstagram"] == 1
clientes[filtro_ins]

# %%
## 04.07 - Quantos clientes possuem exatamente 0 pontos?

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep = ";")
filtro_0 = clientes["qtdePontos"] == 0
clientes[filtro_0]

# %%
## 04.08 - Quantos produtos pertencem à categoria "espada"?
import pandas as pd

produtos = pd.read_csv("../data/produtos.csv", sep = ";")
filtro_esp = produtos["DescCategoriaProduto"] == "espada"
produtos[filtro_esp]

# %%
## 04.09 - Quantos produtos possuem a categoria "poção"?

import pandas as pd

produtos = pd.read_csv("../data/produtos.csv", sep = ";")
filtro_po = produtos["DescCategoriaProduto"] == "poção"
produtos[filtro_po]

# %%
## 04.10 - Quantas transações ocorreram no dia 2025-09-17?

import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv", sep = ";")
transacoes["DtCriacao"] = pd.to_datetime(transacoes["DtCriacao"]).dt.date
filtro_dt = transacoes["DtCriacao"] == pd.to_datetime("2025-09-17").date()
transacoes[filtro_dt]

# %%
## 04.11 - Quantas transações tiveram origem no sistema ""twitch""?

import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv", sep = ";")
filtro_tw = transacoes["DescSistemaOrigem"] == "twitch"
transacoes[filtro_tw]

# %%
## 04.12 - Quantas transações tiveram origem no sistema "youtube"?

import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv", sep = ";")
filtro_yo = transacoes["DescSistemaOrigem"] == "youtube"
transacoes[filtro_yo]

# %%
## 04.13 - Quantos registros existem na tabela transacao_produto
##         onde QtdeProduto é igual a 1?
import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv", sep = ";")
filtro_1 = transacoes["QtdePontos"] == 1
transacoes[filtro_1]