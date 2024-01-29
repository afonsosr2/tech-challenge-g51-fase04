import requests
import pandas as pd
from bs4 import BeautifulSoup
from prophet import Prophet
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.holtwinters import Holt
import joblib

def atualizando_dados_ipea():
    # Função para atualizar DataFrame com novas datas
    def update_dataframe(df, new_data):

        # Converte coluna data para para datetime
        df['Data'] = pd.to_datetime(df['Data'], dayfirst=True)
        new_data['Data'] = pd.to_datetime(new_data['Data'], dayfirst = True)

        # Encontra a data mais recente no Dataframe existente
        last_date = df['Data'].max()

        # Filtra as novas linhas que são mais recentes do que a última data
        new_rows = new_data[new_data['Data'] > last_date]

        # Concatena os novos dados com o dataframe existente se houver novas linhas
        if  not new_rows.empty:
            updated_df = pd.concat([df,new_rows],ignore_index = True)
        else:
            updated_df = df

        return updated_df

    # Base de dados (URL do IPEA)
    url = 'http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view'

    # Faz uma requisição get no site e captura a resposta
    response = requests.get(url)

    # Verifica se a requisição foi bem sucedida
    if  response.status_code ==200:
        # Cria um objeto BeautifulSoup para analisar o HTML
        soup = BeautifulSoup(response.text,'html.parser')

        # Procura pela tabela HTML analisando o id ou classe pode variar
        # Você precisaria inspecionar o HTML para obter o selector correto
        table = soup.find('table',{'id':'grd_DXMainTable'})

        # Usa o pandas para ler a tabela HTML diretamente para um dataframe
        new_df = pd.read_html(str(table),header=0)[0]

        # FOB - Preço de venda da mercadoria, acrescido de todas as despesas do exportador até sua colocação no mercado.
        new_df['Preço - petróleo bruto - Brent (FOB)'] = new_df['Preço - petróleo bruto - Brent (FOB)'] / 100

        # verifca se o dataframe existe: carrega, ou cria um novo Dataframe se não existir
        path ='dados\ipea.csv'
        try:
            existing_df = pd.read_csv(path)
        except FileNotFoundError:
            existing_df = new_df

        # Atualiza o df existente com novos dados (carga incremental)
        updated_df = update_dataframe(existing_df, new_df)
        updated_df = updated_df.sort_values(by="Data", ascending=True).reset_index(drop=True)

        # Salva o DataFrame atualizado para o arquivo
        updated_df.to_csv(path,index=False)
    else:
        print('Falha ao acessar  a página : Status code', response.status_code)
    return path


def retreino_prophet(dados):
    # Criando um df para o formato aceito do Prophet
    df = dados.rename(columns={"Data": "ds", "Preço - petróleo bruto - Brent (FOB)": "y"})

    # Treinando ou Retreinando o modelo
    m = Prophet()
    m.fit(df)

    joblib.dump(m, 'modelo/prophet.joblib')


def retreino_sarimax(dados):
    # Criando um df para o formato aceito do SARIMAX
    dados_resample = dados.set_index("Data").resample('1D').ffill()

    # Treinando ou Retreinando o modelo
    model_sarimax = SARIMAX(dados_resample, order=(3,1,1), seasonal_order=(2,1,0,7))
    model_sarimax.fit()

    joblib.dump(model_sarimax, 'modelo/sarimax.joblib', compress=3)


def retreino_holt(dados):
    # Criando um df para o formato aceito do Holt
    dados_resample = dados.set_index("Data").resample('1D').ffill()

    # Treinando ou Retreinando o modelo
    model_holt = Holt(dados_resample)
    model_holt.fit()

    joblib.dump(model_holt, 'modelo/holt.joblib')