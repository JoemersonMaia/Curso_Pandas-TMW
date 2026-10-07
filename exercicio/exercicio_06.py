##06.01 - Qual a quantidade média de redes sociais dos usuários? E a Variância? E o máximo?
##06.02 - Quais são os usuários que mais fizeram transações? Considere os 10 primeiros.
##06.03 - Qual usuário teve maior quantidade de pontos debitados?
##06.04 - Quem teve mais transações de Streak?
##06.05 - Qual a média de transações / dia?
##06.06 - Como podemos calcular as estatísticas descritivas dos pontos das transações de cada usuário?

# %%
## 06.04 - Quem teve mais transações de Streak?

import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv", sep = ";")
transacoes.head()

transacao_produto = pd.read_csv("../data/transacao_produto.csv", sep = ";")
transacao_produto.head()

produtos = pd.read_csv("../data/produtos.csv", sep = ";")
produtos.head()

# %%
transacao_produto = transacao_produto.rename(columns = {"idTransacao" : "IdTransacao"})
cliente_transaco_produto = transacoes.merge(transacao_produto,
                 on = "IdTransacao",
                 how = "left",
                 )

df_full = cliente_transaco_produto[["IdTransacao", "IdCliente", "IdProduto"]].merge(
    produtos,
    on = ["IdProduto"],
    how = 'left'
)

df_full = df_full[df_full["DescNomeProduto"] == "Presença Streak"]

(df_full.groupby(by = ["IdCliente"])["IdTransacao"]
 .count()
 .sort_values(ascending = False)
 .head(1)
 )

# %%

produtos = produtos[produtos["DescNomeProduto"] == "Presença Streak"]

transacao_produto = transacao_produto.rename(columns = {"idTransacao" : "IdTransacao"})

(transacoes.merge(transacao_produto,on = "IdTransacao",how = "left",)
                 .merge(produtos, on = ["IdProduto"], how = "right") ## se colocar left, os outros produtos vao aparecer null e nao sumir
                 .groupby(by = "IdCliente")["IdTransacao"]
                 .count()
                 .sort_values(ascending = False)
                 .head(1)
                 )

