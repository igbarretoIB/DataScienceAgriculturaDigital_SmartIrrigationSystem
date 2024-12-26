import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pydeck as pdk
import folium
from streamlit_folium import st_folium
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from datetime import datetime
import requests
import joblib
import json    


##### Variaveis de ambiente
CIDADE= 'Luiziânia'
ESTADO= 'São Paulo'
PAIS= 'br'
LATITUDE= -21.6
LONGITUDE= -50.3
TOKEN=''


############# TAB 1 ####################
def Agora():
    # Captura o momento atual
    ag = datetime.now()
    ag= ag.strftime('%H:%M:%S')
    return ag


def DiadaSemana():
    
    # Captura o momento atual
    ag = datetime.now()
    
    # Obtém o dia da semana (0 = segunda-feira, 6 = domingo)
    dia_semana_numero = ag.weekday()

    # Nome do dia da semana (em português)
    dias_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
    dia_semana_nome = dias_semana[dia_semana_numero]
    
    return dia_semana_nome

def returnData():
    # Captura o momento atual
    ag = datetime.now()
    
    # Obtém a data
    data = ag.date()
    
    data = data.strftime("%d-%m-%Y")
    
    return data

def get_Icon(icon):
    dict_wc = { "Thunderstorm":":lightning_cloud:", 
                "Drizzle":":partly_sunny_rain:", 
                "Rain":":rain_cloud:", 
                "Snow":"❄️", 
                "Mist":":fog:", 
                "Smoke":":fog:", 
                "Haze":":fog:", 
                "Dust":":fog:", 
                "Fog":":fog:", 
                "Sand":":fog:", 
                "Ash":":fog:", 
                "Squall":"💨", 
                "Tornado":"🌪️", 
                "Clear":"☀️", 
                "Clouds":"☁️"
    }
    
    return dict_wc.get(icon)

def getWeatherNow(LATITUDE, LONGITUDE, TOKEN):
    # Verificação da condição atual 
    url=f'https://api.openweathermap.org/data/2.5/weather?lat={LATITUDE}&lon={LONGITUDE}&units=metric&appid={TOKEN}'
    response= requests.get(url)
    print(response)
    return response.json()


def getWeatherNow_information(tempo_agora):
    icon = tempo_agora['weather'][0].get('main')
    condicoes= tempo_agora.get('main')
    temperatura=condicoes['temp']
    temp_min=condicoes['temp_min']
    temp_max=condicoes['temp_max']
    umidade=condicoes['humidity']
    vento_vel = tempo_agora.get('wind').get('speed')
    
    return icon, temperatura,temp_min, temp_max, umidade, vento_vel


def getWeatherPrediction(LATITUDE, LONGITUDE, TOKEN, fh=7):
    # Previsão para os próximos 7 dias 
    url= f'https://api.openweathermap.org/data/2.5/forecast?lat={LATITUDE}&lon={LONGITUDE}&cnt={fh}&units=metric&appid={TOKEN}'
    response= requests.get(url)
    print(response)
    return response.json()

def getWeatherPrediction_information(tempo_pred7):
    # Extrair os dados relevantes
    tempo_pred7_data = tempo_pred7['list']
    
    pred7_list = []
    dias_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
    
    # Inicializar variáveis auxiliares
    temp_min = None
    temp_max = None
    icon = None
    
    for data in tempo_pred7_data:
        date_text = data['dt_txt']
        
        # Capturar previsão para 03:00:00
        if date_text.endswith('03:00:00'):
            condicoes = data.get('main')
            temp_min = condicoes['temp_min']
        
        # Capturar previsão para 15:00:00
        elif date_text.endswith('15:00:00'):
            condicoes = data.get('main')
            temp_max = condicoes['temp_max']
            icon = data['weather'][0].get('main')
            
            # Converter data para o formato desejado
            date_object = datetime.strptime(date_text, '%Y-%m-%d %H:%M:%S')
            dia_semana_nome = dias_semana[date_object.weekday()]
            data_ = date_object.date().strftime('%d/%m/%y')
            
            # Adicionar ao resultado
            pred7_list.append({
                dia_semana_nome: {
                    'data': data_,
                    'icon': icon,
                    'temp_min': temp_min,
                    'temp_max': temp_max
                }
            })
    
    data=tempo_pred7_data[-1]       
    date_text= data['dt_txt']
    # Converter o texto para um objeto datetime
    date_object = datetime.strptime(date_text, '%Y-%m-%d %H:%M:%S')
    # Obter o número do dia da semana (0 = segunda-feira, 6 = domingo)
    dia_semana_numero = date_object.weekday()
    data_ = date_object.date().strftime('%d/%m/%y')
    
    # Nome do dia da semana (em português)
    dia_semana_nome = dias_semana[dia_semana_numero]
    icon = data['weather'][0].get('main')
    condicoes= data.get('main')
    temp_max=condicoes['temp_max']
    pred7_list.append({dia_semana_nome:{'data':data_,
                                 'icon': icon, 
                                 'temp_min': temp_min, 
                                 'temp_max': temp_max
                                  }
                                }
                              )

    return pred7_list

def get_weather_description(icon):
    weather_dict = {
        "Thunderstorm": "Tempestade com raios",
        "Drizzle": "Garoa",
        "Rain": "Chuva",
        "Snow": "Neve",
        "Mist": "Névoa",
        "Smoke": "Fumaça",
        "Haze": "Neblina seca",
        "Dust": "Poeira",
        "Fog": "Neblina",
        "Sand": "Areia",
        "Ash": "Cinzas vulcânicas",
        "Squall": "Rajada de vento",
        "Tornado": "Tornado",
        "Clear": "Céu limpo",
        "Clouds": "Nublado"
    }
    
    return weather_dict.get(icon)
def simulate_sensor_data(dataset, new_dataset, i):
    # Captura o momento atual
    ag = datetime.now()
    ag= ag.strftime('%d-%m-%Y %H:%M:%S')
    
    if dataset.iloc[i]['Watering_plant_pump_ON'] == 1.0:
        pump_status = 'On'
    else:
        pump_status = 'Off'
    
    if dataset.iloc[i]['Fan_actuator_ON'] == 1.0:
        fan_status = 'On'
    else:
        fan_status = 'Off'
    
    new_row =  {'data':ag, 
                'temperatura':dataset.iloc[i]['tempreature'], 
                'umidade':dataset.iloc[i]['humidity'], 
                'nivel de agua':dataset.iloc[i]['water_level'], 
                'N':dataset.iloc[i]['N'], 
                'P':dataset.iloc[i]['P'], 
                'K':dataset.iloc[i]['K'],
                'Fan_status':fan_status,
                'Pump_status': pump_status
                }
    
    tempreature= dataset.iloc[i]['tempreature']
    humidity= dataset.iloc[i]['humidity']
    water_level= dataset.iloc[i]['water_level']
    N= dataset.iloc[i]['N']
    P= dataset.iloc[i]['P']
    K= dataset.iloc[i]['K']
    pump_status= dataset.iloc[i]['Watering_plant_pump_ON']
    fan_status= dataset.iloc[i]['Fan_actuator_ON']
    new_dataset=pd.concat([new_dataset, pd.DataFrame([new_row])], ignore_index=True)
    i += 1
    new_row= dataset.iloc[i, 1:-6].values.reshape(1, -1)
    return new_dataset, i, N, P, K, tempreature, humidity, water_level, pump_status, fan_status, new_row



############# TAB 2 ####################
def return_pump_prob(new_row):
    pump_model =  joblib.load('random_forest_model_irrigation.pkl')
    p = pump_model.predict(new_row)
    pump_prob= np.round(p[0],4)*100
    print(p)
    print(pump_prob)
    return pump_prob

def return_fan_prob(new_row):
    fan_model =  joblib.load('random_forest_model_fan.pkl')
    p = fan_model.predict(new_row)
    fan_prob= np.round(p[0],4)*100
    return fan_prob


############# TAB 3 ####################
def plot_radar(data): 
    labels = data['Variáveis'].tolist()
    valores = data['Valores'].tolist() 
    max_valores = [255] * len(labels) 
    
    # Fechar os polígonos 
    valores += valores[:1] 
    max_valores += max_valores[:1] 
    labels += labels[:1] 
    fig = go.Figure() 
    
    # Adicionar o triângulo maior (máximos) 
    fig.add_trace(go.Scatterpolar( r=max_valores, 
                                    theta=labels, 
                                    fill='toself', 
                                    name='Máximo', 
                                    line=dict(color='gray', dash='dash') 
                                    )
                    ) 
    # Adicionar o triângulo menor (valores reais) 
    fig.add_trace(go.Scatterpolar( r=valores, 
                                    theta=labels, 
                                    fill='toself', 
                                    name='Valores Reais', 
                                    line=dict(color='#0A7E31') 
                                    )
                    ) 
    fig.update_layout(polar=dict( bgcolor='#0D1117', 
                                    radialaxis=dict(visible=False), 
                                    angularaxis=dict(tickfont=dict(color='white')) 
                                    ), 
                        showlegend=False, # Remover a legenda 
                        paper_bgcolor='#0D1117', 
                        font=dict(color='white'), 
                        width=800, # Aumentar a largura da área de plotagem 
                        height=800 # Aumentar a altura da área de plotagem 
                        ) 
    return fig


############# TAB 4 ####################

def generate_plot(data, x, y):
    fig = px.line(data, x=x, y=y, title='Gráfico de Linhas', line_shape='linear') #
    fig.update_traces(line=dict(color='green'), mode='lines+markers')
    #fig.update_traces(line=dict(color='#0A7E31', mode='lines+markers'))
    fig.update_layout( plot_bgcolor='#0D1117', paper_bgcolor='#0D1117', font_color='white' ) 
    return fig