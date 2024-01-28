# -*- coding: utf-8 -*-
"""gráficos_techchallenge-4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mmEAAXqpbwF2gAKPDzMKWsTl98YHEIoS
"""

import pandas as pd
import plotly.express as px
import numpy as np
from utils import atualizando_dados_ipea

preco = pd.read_csv(atualizando_dados_ipea())
preco.head()

preco["Data"] = pd.to_datetime(preco["Data"])
preco["Year"] = preco["Data"].dt.year
preco.info()

preco_medio = pd.DataFrame(preco.groupby("Year")["Preço - petróleo bruto - Brent (FOB)"].mean()).reset_index()
preco_medio.head()

fig_1 = px.line(preco_medio, x="Year", y="Preço - petróleo bruto - Brent (FOB)", markers=True)

fig_1.update_layout(
    title="Evolução Preço Petróleo ",
    xaxis_title="Ano",
    yaxis_title="Preço USD",
    font=dict(
        family="Courier New, monospace",
        size=12,
        color="RebeccaPurple"))
# fig_1.show()

producao = pd.read_csv("dados/oil-production-by-country.csv", sep=",", thousands=".")
producao.head()

producao_regiao = producao.set_index("Entity").loc[["South and Central America (EI)","Africa (EI)","Asia Pacific (EI)",
        "Europe (EI)","CIS (EI)","North America (EI)","Middle East (EI)"],["Year","Oil production (TWh)"]]

# Vamos converter Terawatt-hora para Barril de óleo
# 1 TWh = 588.235,29 bboe # Fonte : https://citizenmaths.com/pt/energy-work-heat/terawatt-hours-to-barrels-of-oil-equivalent


producao_regiao["Produção BBOE"] = np.round(producao_regiao["Oil production (TWh)"]*588235.29,1)
producao_regiao.head(5)

fig_2 = px.area(producao_regiao, x="Year", y="Produção BBOE",color= producao_regiao.index, line_group=producao_regiao.index)

fig_2.update_layout(
    title="Produção Barril de Petróleo por Região ",
    xaxis_title="Ano",
    yaxis_title="Produção BBOE",
    legend_title="Região",
    font=dict(
        family="Courier New, monospace",
        size=12,
        color="RebeccaPurple"))
# fig_2.show()

"""Podemos notar que tivemos um crescimento exponencial de produção apartir do ano de 1990
As regiões que mais produzem Petróleo são Oriente Médio , America do Norte e a Comunidade dos Estados idependentes (Cis) que é composta por paises da antiga União Soviética.

A Região (CIS) Comunidade dos Estados Idependentes e o Oriente Médio são regiões de conflitos com alta representatividade em produção , os conflitos impactam nos preços de produção e logistica.

Fonte : https://www.investopedia.com/articles/investing/012216/how-opec-and-nonopec-production-affects-oil-prices.asp
"""

producao_opep = producao.set_index("Entity").loc[["Non-OPEC (EI)","OPEC (EI)"],["Year","Oil production (TWh)"]]
producao_opep["Produção BBOE"] = np.round(producao_opep["Oil production (TWh)"]*588235.29,1)
producao_opep.head()

fig_3 = px.area(producao_opep, x="Year", y="Produção BBOE",color= producao_opep.index, line_group=producao_opep.index)

fig_3.update_layout(
    title="Produção Barril de Petróleo OPEP(OPEC) e NOPEP(Non-OPEC) ",
    xaxis_title="Ano",
    yaxis_title="Produção BBOE",
    legend_title="OPEP e NOPEP",
    font=dict(
        family="Courier New, monospace",
        size=12,
        color="RebeccaPurple"))
# fig_3.show()

"""Os preços do petróleo são influenciados por vários fatores, incluindo oferta e demanda.
Os países membros da Organização dos Países Exportadores de Petróleo (OPEP) produzem cerca de 40% do petróleo bruto mundial.

As exportações de petróleo da OPEP representam aproximadamente 60% do total de petróleo negociado internacionalmente.
A OPEP, especialmente a Arábia Saudita, tem a vantagem na determinação da direção dos preços do petróleo, mas a Rússia também se tornou um ator-chave.

Fonte : https://www.investopedia.com/articles/investing/012216/how-opec-and-nonopec-production-affects-oil-prices.asp
"""

consumo = pd.read_csv("dados/oil-consumption-by-country.csv", sep=",", thousands=".")
consumo.head()

consumo_regiao = consumo.set_index("Entity").loc[["South and Central America (EI)","Africa (EI)","Asia Pacific (EI)",
        "Europe (EI)","CIS (EI)","North America (EI)","Middle East (EI)"],["Year","Oil consumption - TWh"]]

consumo_regiao["Consumo BBOE"] = np.round(consumo_regiao["Oil consumption - TWh"]*588235.29,1)
consumo_regiao.head(5)

fig_4 = px.area(consumo_regiao, x="Year", y="Consumo BBOE",color= consumo_regiao.index, line_group=consumo_regiao.index)

fig_4.update_layout(
    title="Consumo de Barril de Petróleo por Região ",
    xaxis_title="Ano",
    yaxis_title="Consumo BBOE",
    legend_title="Região",
    font=dict(
        family="Courier New, monospace",
        size=12,
        color="RebeccaPurple"))
# fig_4.show()

"""Podemos notar que as regiões que mais consomem Petróleo são a Ásia , América do Norte e Europa
Asia produziu cerca de 2.4 bilhões de barris em 2022 consumiu 11.4 bilhões em 2022 e a Europa produziu 1 bilhão de barris e consumiu 4.7  a Asia e Europa nescessitam de importações e como vimos os maiores Exportadores são os Paises da OPEP que em sua maioria estão no Oriente Médio que é uma região com muitos conflitos e que possui grande poder na decisão no preço de venda.


Podemos notar que o consumo de Petróleo ficou em torno de 33 bilhões de barris em 2022 e a produção total ficou em torno de 30 bilhões a demanda está maior que a oferta puxando os preçoa para cima .
"""


def plotar_graf(x) :
  if x==1 :
    return fig_1
  elif x==2 :
    return fig_2
  elif x==3 :
    return fig_3
  elif x==4 :
    return fig_4
  else:
    print("Escolha um gráfico entre 1 e 4")
