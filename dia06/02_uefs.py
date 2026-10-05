# %%

import pandas as pd

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"

dfs = pd.read_html(url)
uf = dfs[0]
# %%

import pandas as pd
import requests
from io import StringIO

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"

headers = {
    "User-Agent": "Mozilla/5.0"
}

resposta = requests.get(url, headers=headers)

dfs = pd.read_html(StringIO(resposta.text))
uf = dfs[1]

# %%
def str_to_float(x:str):
    x = float(x.replace(" ", "")
              .replace(",", ".")
              .replace("\xa0", ""))
    return x

uf["Área (km²)"] = uf["Área (km²)"].apply(str_to_float)
uf["População (Censo 2022)"] = uf["População (Censo 2022)"].apply(str_to_float)
uf["PIB (2015)"] = uf["PIB (2015)"].apply(str_to_float)
uf["PIB per capita (R$) (2015)"] = uf["PIB per capita (R$) (2015)"].apply(str_to_float)

# %%
def strex_to_float(x:str):
    x = float(x.replace(" ", "")
              .replace("anos", "")
              .replace(",", "."))
    return x

uf["Expectativa de vida (2016)"] = uf["Expectativa de vida (2016)"].apply(strex_to_float)

#%%

def srt_to_por(x:str):
    x = float(x.replace("%", "")
              .replace(",", "."))
            
    return x

uf["Alfabetização (2016)"] = uf["Alfabetização (2016)"].apply(srt_to_por)

# %%

def str_to_porin(x:str):
    x = float(x.replace(",", ".")
              .replace("‰", ""))
    return x

uf["Mortalidade infantil (/1000)"] = uf["Mortalidade infantil (2016)"].apply(str_to_porin)

uf

# %%

def uf_to_regiao(uf):
    if uf in ["Distrito Federal", "Goiás", "Mato Grosso", "Mato Grosso do Sul"]:
        return "Centro-Oeste"

    elif uf in ["Alagoas", "Bahia", "Ceará", "Maranhão", "Paraíba", "Pernambuco", "Piauí",
                 "Rio Grande do Norte", "Sergipe"]:
        return "Nordeste"

    elif uf in ["Acre", "Amapá", "Amazonas", "Pará", "Rondônia", "Roraima", "Tocantins"]:
        return "Norte"

    elif uf in ["Espírito Santo", "Minas Gerais", "Rio de Janeiro", "São Paulo"]:
        return "Sudeste"

    elif uf in ["Paraná", "Rio Grande do Sul", "Santa Catarina"]:
        return "Sul"


uf["Região"] = uf["Unidade federativa"].apply(uf_to_regiao)

# %%

def classica_bom(linha):
    return (linha["PIB per capita (R$) (2015)"] > 30000 and
    linha["Mortalidade infantil (/1000)"] < 15 and 
    linha["IDH (2010)"] > 700)

uf["classificacao"] = uf.apply(classica_bom, axis = 1)
# %%
uf