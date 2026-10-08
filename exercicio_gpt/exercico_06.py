##06.01 - Qual a quantidade média de redes sociais dos usuários? E a Variância? E o máximo?
##06.02 - Quais são os usuários que mais fizeram transações? Considere os 10 primeiros.
##06.03 - Qual usuário teve maior quantidade de pontos debitados?

# %%
import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv", sep = ";")
transacoes.head()

# %%

(transacoes.groupby(by = "IdCliente")["IdTransacao"]
                                    .count()
                                    .sort_values(ascending = False)
                                    .head(10))

# %%
##06.02 - Quais são os usuários que menos fizeram transações? Considere os 10 primeiros.

import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv", sep = ";")
transacoes.head()

# %%

(transacoes.groupby(by = ["IdCliente"])["IdTransacao"]
                                        .count()
                                        .sort_values()
                                        .head(10)
                                        )

# %%
##06.03 - Qual usuário teve maior quantidade de pontos debitados?

import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv", sep = ";")
transacoes.head()

# %%
filtro = transacoes["QtdePontos"] < 0
(transacoes[filtro].groupby(by = ["IdCliente"])["QtdePontos"]
                                                .sum()
                                                .sort_values()
                                                .head(1)
                                                )


# %%

##06.04 - Quem teve mais transações de armadura?

import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv", sep = ";")
transacoes.head()

# %%

transacao_produto = pd.read_csv("../data/transacao_produto.csv", sep = ";")
transacao_produto.head()

# %%

produtos = pd.read_csv("../data/produtos.csv", sep = ";")
filtro = produtos["DescCategoriaProduto"] == "armadura"
produtos[filtro]

# %%
clliente_transacao_produto = transacoes.merge(transacao_produto,
                                             on = "IdTransacao",
                                             how = "left"
                                                )

#%%

df_full = clliente_transacao_produto.merge(produtos,
                                           on = "IdProduto",
                                           how = "left"
                                           )
filtro = df_full["DescCategoriaProduto"] == "chat"
df_full = df_full[filtro]
(df_full[["IdCliente", "IdTransacao", "DescCategoriaProduto"]].groupby(by = ["IdCliente"])["IdTransacao"]
                                                                                           .count()
                                                                                           .sort_values(ascending = False)
                                                                                           .head(10))

# %%

produtos = produtos[produtos["DescCategoriaProduto"] == "espada"]
produtos

(transacoes.merge(transacao_produto, on = "IdTransacao", how = "left")
            .merge(produtos, on = "IdProduto", how = "right")
            .groupby(by = ["IdCliente"])["IdTransacao"]
            .count()
            .sort_values(ascending = False)
            .head(10))

# %%

##06.05 - Qual a média de transações / dia?

import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv", sep = ";")
transacoes.head()

# %%
transacoes["DtDia"] = pd.to_datetime(transacoes["DtCriacao"]).dt.date
transacoes

# %%
summary = (transacoes.groupby(by = ["DtDia"])
           .agg({
               "IdTransacao" : "count",
           }))
summary.mean()

# %%
##06.04 - Quem teve mais transações de Espada Longa?
 
import pandas as pd 

transacoes = pd.read_csv("../data/transacoes.csv", sep = ";")
transacoes.head()

# %%
transacao_produto = pd.read_csv("../data/transacao_produto.csv", sep = ";")
transacao_produto.head()

# %%

produtos = pd.read_csv("../data/produtos.csv", sep = ";")
produtos.head()

# %%

cliente_transacao_produto = transacoes.merge(transacao_produto,
                                             on = "IdTransacao", 
                                             how = "left")
cliente_transacao_produto.head()

# %%

df_full = cliente_transacao_produto.merge(produtos,
                                          on="IdProduto",
                                          how = "left"
                                            )

df_full.head()

# %%

df_full = df_full[df_full["IdProduto"] == "6"]
(df_full.groupby(by = ["IdCliente"])["IdTransacao"]
                                    .count()
                                    .sort_values(ascending = False)
                                    .head(10))

# %%

produtos = produtos[produtos["IdProduto"] == "6"]

transacao_produto = transacao_produto.rename(columns = {"idTransacao" : "IdTransacao"})

(transacoes.merge(transacao_produto, on = "IdTransacao", how = "left")
            .merge(produtos, on = "IdProduto", how = "right")
            .groupby("IdCliente")["IdTransacao"]
            .count()
            .sort_values(ascending=False)
            .head(10)
            )

