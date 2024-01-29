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
st.write("Em construção!")
