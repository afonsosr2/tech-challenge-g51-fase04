import streamlit as st

###### Páginal Inicial do Streamlit ######
st.set_page_config(layout= 'wide')
st.title(":oil_drum: Análise de preços do Petróleo Brent")

st.header("Sobre o MVP", divider="gray")

st.markdown('''
            Como consultores fomos requisitados para analisar os dados do preço do **Petróleo Brent**.  
             Por isso, desenvolvemos no aplicativo do Streamlit um MVP que demonstra ao menos três etapas do projeto:
            - **Homepage:** Resumo do projeto e fluxograma da obtenção dos dados, geração do modelo, carga do modelo, API e Dashboard
            - **Dashboard:** Dashboard analisando os dados do petróleo em todo mundo e possíveis insights para a evolução dos preço do Petróleo Brent
            - **Modelos de previsão:** Com os modelos para prever o preço do Petróleo Brent com os filtros desejados
            e com métricas de avaliação dos modelos.
            
            Esse dashboard do Streamlit gera insights relevantes para a tomada de decisão da empresa.
            
            Sinta-se livre para explorar este ambiente! :computer:
            ''')

st.markdown('''<style>
[data-testid="stMarkdownContainer"] ul{
    list-style-position: inside;
}</style>''', 
unsafe_allow_html=True)

st.header("Fluxograma do MVP", divider="gray")
st.image("Fluxo do dados.drawio.png", caption = 'Fluxograma dos dados do MVP')

st.header('Referências', divider = "gray")

st.markdown('''
            - PANDAS. Documentação da biblioteca Pandas [Internet]. [acessado 2023 Jan].  
             Disponível em: https://pandas.pydata.org/docs/reference/
            - STREAMLIT. Documentação da biblioteca Streamlit [Internet]. [acessado 2023 Jan].  
            Disponível em: https://docs.streamlit.io/
            - PROPHET. Documentação da biblioteca Prophet [Internet]. [acessado 2023 Jan].  
            Disponível em: https://facebook.github.io/prophet/docs/quick_start.html
            - STATSMODELS. Documentação da biblioteca Statsmodels [Internet]. [acessado 2023 Jan].  
            Disponível em: https://www.statsmodels.org/stable/index.html
            - JOBLIB. Documentação da biblioteca Joblib [Internet]. [acessado 2023 Jan].  
            Disponível em: https://joblib.readthedocs.io/en/stable/
            - PLOTLY. Documentação da biblioteca Plotly [Internet]. [acessado 2023 Jan].  
            Disponível em: https://plotly.com/python/
            - JOEL, Grus. Data Science do Zero: Noções Fundamentais com Python [Livro físico]
            - KNAFLIC, Cole Nussbaumer. Storytelling com dados: uma guia sobre visualização de dados para profissionais de negócio [Livro físico]
            - IPEA, Preço por barril do petróleo bruto Brent (FOB)[Internet]. [acessado 2023 Jan].  
            Disponível em: http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view
            - OUR WORLD IN DATA. Oil production (em inglês) [Internet]. [acessado 2023 Jan].  
            Disponível em: https://ourworldindata.org/grapher/oil-production-by-region
            - OUR WORLD IN DATA. Oil consumption (em inglês)[Internet]. [acessado 2023 Jan].  
            Disponível em: https://ourworldindata.org/grapher/oil-consumption-by-region-terawatt-hours-twh
            - CITIZENMATHS. Terawatt-hora para Barril de óleo equivalente conversões [Internet]. [acessado 2023 Jan].  
            Disponível em: https://citizenmaths.com/pt/energy-work-heat/terawatt-hours-to-barrels-of-oil-equivalent
            - INVESTOPEDIA. How OPEC (and Non-OPEC) Production Affects Oil Prices (em inglês) [Internet]. [acessado 2023 Jan].  
            Disponível em: https://www.investopedia.com/articles/investing/012216/how-opec-and-nonopec-production-affects-oil-prices.asp
            - WIKIPEDIA. List of countries by oil exports (em inglês) [Internet]. [acessado 2023 Jan].  
            Disponível em: https://en.wikipedia.org/wiki/List_of_countries_by_oil_exports           
            ''')
