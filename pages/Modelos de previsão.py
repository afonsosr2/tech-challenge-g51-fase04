import streamlit as st
import pandas as pd
import numpy as np
import datetime
import joblib
from prophet.plot import plot_plotly
from plotly import graph_objs as go
from utils import atualizando_dados_ipea, retreino_prophet, retreino_sarimax, retreino_holt 

###### Configuração Inicial ######
@st.cache_data
def config_inicial():
    dados = pd.read_csv(atualizando_dados_ipea(), parse_dates=["Data"])
    retreino_prophet(dados)
    retreino_sarimax(dados)
    retreino_holt(dados)
    return dados

def formata_numero(valor, prefixo = ''):
    if(isinstance(valor, datetime.datetime)):
        return valor.strftime('%d/%m/%Y')
    return f'{prefixo} {valor:.2f}'

###### Modelos ######

# Previsão com Prophet
def prophet_prediction(periodo_previsao):
    # Carregando o modelo
    m = joblib.load('modelo/prophet.joblib')

    # Prevendo de acordo com o filtro
    future = m.make_future_dataframe(periods=periodo_previsao, freq="B")
    forecast = m.predict(future)
    forecast_resumo = forecast[["ds", "yhat"]].rename(columns=
                                                      {"ds": "Data", 
                                                       "yhat": "Preço - petróleo bruto - Brent (FOB)"})
    return m, forecast, forecast_resumo

# Previsão com Modelo 1
def sarimax_prediction(periodo_previsao):
    # Carregando o modelo
    sarimax = joblib.load('modelo/sarimax.joblib')

    # Prevendo de acordo com o filtro
    sarimax_results= sarimax.fit()
    forecast_sarimax = sarimax_results.get_forecast(steps=periodo_previsao)
    forecast_medio = forecast_sarimax.predicted_mean

    st.subheader('Previsão')
    forecast = forecast_medio.reset_index()
    forecast = forecast.rename(columns={"index": "Data",
                                        "predicted_mean":"Preço - petróleo bruto - Brent (FOB)"})
  
    return forecast

def holt_prediction(periodo_previsao):
    # Carregando o modelo
    holt = joblib.load('modelo/holt.joblib')

    # Prevendo de acordo com o filtro
    holt_results= holt.fit()
    forecast_holt = holt_results.forecast(periodo_previsao)
    
    st.subheader('Previsão')
    forecast = forecast_holt.reset_index()
    forecast = forecast.rename(columns={"index": "Data",
                                        0:"Preço - petróleo bruto - Brent (FOB)"})
    return forecast

###### Gráficos e Métricas ######

# Gráfico dos dados brutos
def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dados['Data'], y=dados['Preço - petróleo bruto - Brent (FOB)'], name="Preço do Petróleo Brent"))
    fig.layout.update(title_text='Preço do Petróleo Brent (FOB)', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

# Gráfico da previsão com Prophet    
def prophet_plot_table(m, forecast, forecast_resumo, periodo_previsao):
    # Mostrando os últimos 5 dias de previsão e plotando o gráfico com a previsão e dados do IPEA
    st.subheader('Previsão')
    st.dataframe(forecast_resumo.round(2).tail())
        
    st.subheader(f'Gráfico de previsão em {periodo_previsao} dias')
    plot_prev_prophet = plot_plotly(m, forecast)
    st.plotly_chart(plot_prev_prophet)

# Gráfico da previsão com SARIMAX
def sarimax_plot_table(forecast, periodo_previsao):
    # Mostrando os últimos 5 dias de previsão e plotando o gráfico com a previsão e dados do IPEA
    st.subheader('Previsão')
    st.dataframe(forecast.round(2).tail())

    dados_resumidos = dados.query("Data >= '2020-01-01'")

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dados_resumidos["Data"], y=dados_resumidos['Preço - petróleo bruto - Brent (FOB)'], name="Preço do Petróleo Brent"))
    fig.add_trace(go.Scatter(x=forecast["Data"], y=forecast['Preço - petróleo bruto - Brent (FOB)'], name="Previsão do preço"))
    fig.layout.update(title_text=f'Gráfico de previsão em {periodo_previsao} dias', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

# Gráfico da previsão com o Modelo de Suavização Holt
def holt_plot_table(forecast, periodo_previsao):
    # Mostrando os últimos 5 dias de previsão e plotando o gráfico com a previsão e dados do IPEA
    st.subheader('Previsão')
    st.dataframe(forecast.round(2).tail())

    dados_resumidos = dados.query("Data >= '2020-01-01'")

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dados_resumidos["Data"], y=dados_resumidos['Preço - petróleo bruto - Brent (FOB)'], name="Preço do Petróleo Brent"))
    fig.add_trace(go.Scatter(x=forecast["Data"], y=forecast['Preço - petróleo bruto - Brent (FOB)'], name="Previsão do preço"))
    fig.layout.update(title_text=f'Gráfico de previsão em {periodo_previsao} dias', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

# Criando uma função wmape
def wmape(y_true, y_pred):
    return np.abs(y_true-y_pred).sum() / np.abs(y_true).sum()

# Métricas do Prophet
def prophet_metrics():
     # Performance da técnica
    df_result = {"MAE": 6.50705,
                 "MSE": 62.59873,
                 "RMSE": 7.91194,
                 "MAPE": "8.27%",
                 "WMAPE": "7.92%"}
    index = ["Prophet"]
    resultados = pd.DataFrame(df_result, index=index)

    st.subheader('Métricas do modelo treinado para os dados até 22/01/2024')
    st.caption('Para mais informações consultar o arquivo **modelos.ipynb** do repositório')
    st.dataframe(resultados)

# Métricas do Sarimax
def sarimax_metrics():
    # Performance da técnica
    df_result = {"MAE": 1.10265,
                 "MSE": 2.11869,
                 "RMSE": 1.45557,
                 "MAPE": "1.40%",
                 "WMAPE": "65.70%"}
    index = ["SARIMAX"]
    resultados = pd.DataFrame(df_result, index=index)

    st.subheader('Métricas do modelo treinado para os dados até 22/01/2024')
    st.caption('Para mais informações consultar o arquivo **modelos.ipynb** do repositório')
    st.dataframe(resultados)

# Métricas do Holt
def holt_metrics():
    # Performance da técnica
    df_result = {"MAE": 1.50744,
                 "MSE": 4.07913,
                 "RMSE":7.91194,
                 "MAPE": "1.94%",
                 "WMAPE": "57.25%"}
    index = ["Holt"]
    resultados = pd.DataFrame(df_result, index=index)

    st.subheader('Métricas do modelo treinado para os dados até 22/01/2024')
    st.caption('Para mais informações consultar o arquivo **modelos.ipynb** do repositório')
    st.dataframe(resultados)

###### Página dos Modelos de Previsão ######
    
#### Sidebar ####
    
st.sidebar.title('Parâmetros do Modelo')
with st.sidebar.expander('Período de Previsão', True):
    periodo = st.slider('Selecione o período de previsão:', 1, 30, 7)

with st.sidebar.expander('Modelo de Machine Learning', True):
    input_modelo = st.selectbox('Selecione o modelo que deseja utilizar:', ['Escolha um modelo','SARIMAX', 'Prophet', 'Holt'], 0)

rodar_modelo = st.sidebar.button(label="Rodar Modelo")

#### Página dos modelos de previsão do petróleo Brent ####
# Função que roda as configurações iniciais
# Leitura dos dados do IPEA, treino e retreino de modelos 
dados = config_inicial()

# Início do site
st.write('# :oil_drum: Análise de preços do Petróleo Brent')
st.header("Dados do Petróleo Brent", divider="gray")

# Dados da última atualização dos dados
coluna1, coluna2 = st.columns(2)
with coluna1:
    st.metric('Data da última atualização dos dados:', formata_numero(dados["Data"].max()))
with coluna2:
    st.metric('Preço da última atualização dos dados:', formata_numero(dados['Preço - petróleo bruto - Brent (FOB)'].iloc[-1], "U$"))

# Gráfico dos dados atuais  
plot_raw_data()

# Escolha do modelo - Libera parte da página destinada ao modelo escolhido

# Padrão
if(input_modelo == "Escolha um modelo"):
    st.info("Defina o modelo, os parâmetros e rode o modelo para exibição dos dados\n", icon="🚨")

# Prophet
if(input_modelo == "Prophet" and rodar_modelo):
    st.header("Prophet", divider="gray")
    m, forecast, forecast_resumo = prophet_prediction(periodo)

    aba1, aba2 = st.tabs(['Resultado', 'Métricas do modelo'])
    with aba1:
        prophet_plot_table(m, forecast, forecast_resumo, periodo)
    with aba2:
        prophet_metrics()

# SARIMAX
if(input_modelo == "SARIMAX" and rodar_modelo):
    st.header("SARIMAX", divider="gray")
    forecast = sarimax_prediction(periodo)
    
    aba1, aba2 = st.tabs(['Resultado', 'Métricas do modelo'])
    with aba1:
        sarimax_plot_table(forecast, periodo)
    with aba2:
        sarimax_metrics()

# HOLT
if(input_modelo == "Holt" and rodar_modelo):
    st.header("Holt", divider="gray")
    forecast = holt_prediction(periodo)
    
    aba1, aba2 = st.tabs(['Resultado', 'Métricas do modelo'])
    with aba1:
        holt_plot_table(forecast, periodo)
    with aba2:
        holt_metrics()
