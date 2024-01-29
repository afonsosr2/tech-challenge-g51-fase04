### Tech Challenge - Análise dos preços do Petróleo Brent

### Notebooks e Arquivos.py 📓

Os notebooks utilizados no projeto são:
- [modelos.ipynb](https://github.com/afonsosr2/tech-challenge-g51-fase04/blob/main/notebooks/modelos.ipynb) - Representando os modelos treinados de previsão dos preços do Petróleo Brent 
- [gráfico.py](https://github.com/afonsosr2/tech-challenge-g51-fase04/blob/main/grafico.py) - Código Python para geração dos gráficos da página Dashboard do Streamlit
- [utils.py](https://github.com/afonsosr2/tech-challenge-g51-fase04/blob/main/utils.py) - Código Python para atualização dos dados do IPEA e treino e retreino dos modelos

### Dados 🎲

Os dados principais foram obtidos no [IPEA (Instituto de Pesquisa Econômica Aplicada)](http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view)

Outros dados foram:
- [Produção de Petróleo por região](https://ourworldindata.org/grapher/oil-production-by-region)
- [Consumo de Petróleo por região](https://ourworldindata.org/grapher/oil-consumption-by-region-terawatt-hours-twh)
- [Conversão de Terawatt-hora por barril de petróleo](https://citizenmaths.com/pt/energy-work-heat/terawatt-hours-to-barrels-of-oil-equivalent)
- [Informações sobre mercado e exportação de Petróleo](https://www.investopedia.com/articles/investing/012216/how-opec-and-nonopec-production-affects-oil-prices.asp)
- [Lista de países por exportação de petróleo](https://en.wikipedia.org/wiki/List_of_countries_by_oil_exports)

> Os dados estão disponíveis na pasta [dados](https://github.com/afonsosr2/tech-challenge-g51-fase04/tree/main/dados) deste repositório. 

### Aplicação 📲
Você pode acessar a aplicação criada [aqui](https://tech-challenge-g51-fase04.streamlit.app/). 

### Objetivo 🎯
Como consultores fomos requisitados por um cliente do segmento de Petróleo e Gás para analisar os dados do preço do petróleo brent. A demanda é desenvolver um dashboard por meio do Streamlit para gerar insights relevantes para a tomada de decisão da empresa. Para isso, vamos desenvolver um modelo de Machine Learning a fim de realizar o forecasting (previsão) do preço deste tipo de petróleo.
 
