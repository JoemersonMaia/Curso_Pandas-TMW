# %%

import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv", sep = ";")
clientes = pd.read_csv("../data/clientes.csv", sep = ";")

# %%
clientes = clientes.rename(columns = {"idCliente" : "IdCliente", "qtdePontos" : "QtdePontos"})

transacoes.merge(right = clientes, 
                 how = 'left', 
                 on = ['IdCliente'],
                 suffixes = ["Transacao", "Cliente"]
                 )


# %%

df_1 = pd.DataFrame({
    "transacoes" : [1,2,3,4,5],
    "nome" : ["t1", "t2", "t3", "t4", "t5"],
    "IdCliente" : [1,2,3,4,5],
    "valor" : [11,22,33,44,55],
})

df_2 = pd.DataFrame({
    "Id" : [1,2,3,4],
    "nome" : ["teo", "flavia", "mah", "joao"],
})

df_1.merge(df_2, left_on = ["IdCliente"], right_on = ["Id"],
           how = "left",
           suffixes = ["transacao", "cliente"])

# %%