##03.01 - Quantas linhas há no arquivo clientes.csv ?
##03.02 - Quantas colunas do tipo int há no arquivo transacoes.csv ?
##03.03 - Quantas colunas do tipo object há no arquivo produtos.csv ?
##03.04 - Qual o id do cliente no índice 4 no arquivo clientes.csv ?
##03.05 - Qual o saldo de pontos do cliente na 10a posição (sem or
##                                denar) do arquivo clientes.csv ?


# %%
import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep = ";")
clientes.shape

# %%
clientes.info()

# %%
import pandas as pd 

transacoes = pd.read_csv("../data/transacoes.csv", sep = ";")

filtro_int = transacoes.select_dtypes("int64")
filtro_obj = transacoes.select_dtypes("object")
filtro_obj.info()
filtro_int.info()

# %%

clientes.iloc[3]

# %%
clientes.sort_values(by = ["qtdePontos"], ascending=[False]).head(5)

## 03.06 - Quantas linhas há no arquivo transacoes.csv ?

## 03.07 - Quantas colunas há no arquivo produtos.csv ?

## 03.08 - Quantas colunas do tipo float64 há no arquivo clientes.csv ?

## 03.09 - Qual o nome da primeira coluna do arquivo clientes.csv ?

## 03.10 - Qual o nome da última coluna do arquivo produtos.csv ?

## 03.11 - Qual o id do produto que está no índice 5 no arquivo produtos.csv ?

## 03.12 - Qual o nome do cliente que está na 8ª posição
##         (sem ordenar) do arquivo clientes.csv ?

## 03.13 - Qual o preço do produto que está na 12ª posição
##         (sem ordenar) do arquivo produtos.csv ?

## 03.14 - Qual o saldo de pontos do cliente que está no índice 15
##         no arquivo clientes.csv ?

## 03.15 - Quantas colunas do tipo object há no arquivo transacoes.csv ?


# %%

## 03.06 - Quantas linhas há no arquivo transacoes.csv ?

import pandas as pd

transacoes = pd.read_csv("../data/transacoes.py")
transacoes.shape