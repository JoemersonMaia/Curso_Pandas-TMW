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
clientes.info()

filtro_int = clientes.select_dtypes(include = 'int64')
filtro_obj = clientes.select_dtypes(include = 'object')

filtro_obj

# %%

clientes.iloc[3]

# %%
posicao = clientes.iloc[9]
clientes.sort_values(by="idCliente")