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

transacoes = pd.read_csv("../data/transacoes.csv")
transacoes.shape

# %%

## 03.07 - Quantas colunas há no arquivo produtos.csv ?

import pandas as pd

produtos = pd.read_csv("../data/produtos.csv", sep = ";")
produtos.columns

# %%

## 03.08 - Quantas colunas do tipo float64 há no arquivo clientes.csv ?

import pandas as pd 

clientes = pd.read_csv("../data/clientes.csv", sep = ";")
clientes.select_dtypes("int64")

# %%

## 03.09 - Qual o nome da primeira coluna do arquivo clientes.csv ?

import pandas as pd 

clientes = pd.read_csv("../data/clientes.csv", sep = ";")
clientes.columns[0]

# %%

## 03.10 - Qual o nome da última coluna do arquivo produtos.csv ?

import pandas as pd

produtos = pd.read_csv("../data/clientes.csv", sep = ";")
produtos.columns[-1]

# %%

## 03.11 - Qual o id do produto que está no índice 5 no 
# arquivo produtos.csv ?

import pandas as pd

produtos = pd.read_csv("../data/produtos.csv", sep = ";")
produtos.iloc[4]

# %%

## 03.12 - Qual o nome do cliente que está na 8ª posição
##         (sem ordenar) do arquivo clientes.csv ?

import pandas as pd 

clientes = pd.read_csv("../data/clientes.csv", sep = ";")
clientes.iloc[7]

# %%

## 03.13 - Qual o preço do produto que está na 12ª posição
##         (sem ordenar) do arquivo produtos.csv ?

import pandas as pd 

produtos = pd.read_csv("../data/produtos.csv", sep = ";")
produtos.iloc[11]

# %%

## 03.14 - Qual o saldo de pontos do cliente que está no índice 15
##         no arquivo clientes.csv ?

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep = ";")
clientes.iloc[4]

## 03.15 - Quantas colunas do tipo object há no arquivo 
# transacoes.csv ?

import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv", sep = ";")
transacoes.select_dtypes("object").info()


## 03.16 - Quantas colunas do tipo int64 há no arquivo clientes.csv ?

## 03.17 - Qual o tipo de dado da coluna idCliente no arquivo clientes.csv ?

## 03.18 - Qual o tipo de dado da coluna valor no arquivo transacoes.csv ?

# %%

## 03.16 - Quantas colunas do tipo int64 há no arquivo clientes.csv ?

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep = ";")
clientes.select_dtypes("int64").info()

# %%
## 03.17 - Qual o tipo de dado da coluna idCliente no arquivo clientes.csv ?

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep = ";")
clientes.info()

# %%

## 03.18 - Qual o tipo de dado da coluna valor no arquivo transacoes.csv ?

