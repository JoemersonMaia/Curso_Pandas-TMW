# %%

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep =";")

max_ponto = clientes["qtdePontos"].max()
filtro = clientes["qtdePontos"] == max_ponto
clientes[filtro]

# %%

top_5 = (clientes.sort_values(by = "qtdePontos", ascending = False)
    .head(5)["idCliente"])

type(top_5)

# %%

clientes

 # %%

brinquedo = pd.DataFrame(
  {
   "nome": ["teo", "flavia", "maria", "joao"],
   "idade" : [10,30,20,22],
   "salario" : [1000,2000,3000,3000]
  }
 )

# %%

brinquedo.sort_values(by=["salario", "idade"], ascending=[False,True])