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
from datetime import datetime, timedelta
import time
import requests
import json
import joblib
from PIL import Image
import SmartIrrigationSystem as sis



# Configurar layout da página como wide
st.set_page_config(layout="wide")


def time_():
    # Pausar por 10 segundos
    time.sleep(10)
    return st.rerun()
##### Variaveis de ambiente
CIDADE= 'Luiziânia'
ESTADO= 'SP'
PAIS= 'br'
LATITUDE= -21.6
LONGITUDE= -50.3
TOKEN='4970da017dd95b5934d38c4a0559aa29'


##### Variaveis do streamlit

if 'tempo_agora' not in st.session_state:
    st.session_state.tempo_agora = None

if 'previsao_tempo' not in st.session_state:
    st.session_state.previsao_tempo = []

if 'dia_1' not in st.session_state:
    st.session_state.dia_1 = ""
if 'data_1' not in st.session_state:
    st.session_state.data_1 = ""
if 'icon_1' not in st.session_state:
    st.session_state.icon_1 = ""
if 'tmin_1' not in st.session_state:
    st.session_state.tmin_1 = ""
if 'tmax_1' not in st.session_state:
    st.session_state.tmax_1 = ""

if 'dia_2' not in st.session_state:
    st.session_state.dia_2 = ""
if 'data_2' not in st.session_state:
    st.session_state.data_2 = ""
if 'icon_2' not in st.session_state:
    st.session_state.icon_2 = ""
if 'tmin_2' not in st.session_state:
    st.session_state.tmin_2 = ""
if 'tmax_2' not in st.session_state:
    st.session_state.tmax_2 = ""

if 'dia_3' not in st.session_state:
    st.session_state.dia_3 = ""
if 'data_3' not in st.session_state:
    st.session_state.data_3 = ""
if 'icon_3' not in st.session_state:
    st.session_state.icon_3 = ""
if 'tmin_3' not in st.session_state:
    st.session_state.tmin_3 = ""
if 'tmax_3' not in st.session_state:
    st.session_state.tmax_3 = ""

if 'dia_4' not in st.session_state:
    st.session_state.dia_4 = ""
if 'data_4' not in st.session_state:
    st.session_state.data_4 = ""
if 'icon_4' not in st.session_state:
    st.session_state.icon_4 = ""
if 'tmin_4' not in st.session_state:
    st.session_state.tmin_4 = ""
if 'tmax_4' not in st.session_state:
    st.session_state.tmax_4 = ""

if 'dia_5' not in st.session_state:
    st.session_state.dia_5 = ""
if 'data_5' not in st.session_state:
    st.session_state.data_5 = ""
if 'icon_5' not in st.session_state:
    st.session_state.icon_5 = ""
if 'tmin_5' not in st.session_state:
    st.session_state.tmin_5 = ""
if 'tmax_5' not in st.session_state:
    st.session_state.tmax_5 = ""

if 'dia_6' not in st.session_state:
    st.session_state.dia_6 = ""
if 'data_6' not in st.session_state:
    st.session_state.data_6 = ""
if 'icon_6' not in st.session_state:
    st.session_state.icon_6 = ""
if 'tmin_6' not in st.session_state:
    st.session_state.tmin_6 = ""
if 'tmax_6' not in st.session_state:
    st.session_state.tmax_6 = ""

if 'data_hoje' not in st.session_state:
    st.session_state.data_hoje = None
    
if 'dia_semana' not in st.session_state:
    st.session_state.dia_semana = ""   

if 'hora' not in st.session_state:
    st.session_state.hora = ""

if 'icon_hoje' not in st.session_state:
    st.session_state.icon_hoje = ""

if 'hoje_desc' not in st.session_state:
    st.session_state.hoje_desc = ""
    
if 'tmin_hoje' not in st.session_state:
    st.session_state.tmin_hoje = ""

if 'tmax_hoje' not in st.session_state:
    st.session_state.tmax_hoje = ""    
    
if 'tmed_hoje' not in st.session_state:
    st.session_state.tmed_hoje = ""

if 'umidade_hoje' not in st.session_state:
    st.session_state.umidade_hoje = ""
    
if 'vento_hoje' not in st.session_state:
    st.session_state.vento_hoje = ""
    
    
if 'tmin_hoje_list' not in st.session_state:
    st.session_state.tmin_hoje_list = [0]

if 'tmax_hoje_list' not in st.session_state:
    st.session_state.tmax_hoje_list = [0] 
    
if 'tmed_hoje_list' not in st.session_state:
    st.session_state.tmed_hoje_list =  [0] 

if 'umidade_hoje_list' not in st.session_state:
    st.session_state.umidade_hoje_list =  [0] 
    
if 'vento_hoje_list' not in st.session_state:
    st.session_state.vento_hoje_list =  [0] 
    
if 'tmin_hoje_delta' not in st.session_state:
    st.session_state.tmin_hoje_delta = ""

if 'tmax_hoje_delta' not in st.session_state:
    st.session_state.tmax_hoje_delta = "" 
    
if 'tmed_hoje_delta' not in st.session_state:
    st.session_state.tmed_hoje_delta =  ""

if 'umidade_hoje_delta' not in st.session_state:
    st.session_state.umidade_hoje_delta = "" 
    
if 'vento_hoje_delta' not in st.session_state:
    st.session_state.vento_hoje_delta = "" 
    
# Inicializar o estado da sessão para armazenar o dataset
if "new_dataset" not in st.session_state:
    st.session_state.new_dataset = pd.DataFrame(columns=['data', 
                                   'temperatura', 
                                   'umidade', 
                                   'nivel de agua', 
                                   'N', 
                                   'P', 
                                   'K',
                                   'Fan_status',
                                   'Pump_status', 
                                   ]
                          )
if "dataset" not in st.session_state:
    st.session_state.dataset = pd.read_csv('IoTProcessed_Data.csv', sep=',')
    
if "contador" not in st.session_state:
    st.session_state.contador= 0
    
if "temperatura_estufa" not in st.session_state:
    st.session_state.temperatura_estufa= ""
    
if "umidade_estufa" not in st.session_state:
    st.session_state.umidade_estufa= ""
    
if "nivel_agua_estufa" not in st.session_state:
    st.session_state.nivel_agua_estufa= ""

if "N" not in st.session_state:
    st.session_state.N= ""
    
if "P" not in st.session_state:
    st.session_state.P= ""

if "K" not in st.session_state:
    st.session_state.K= ""

if "fan_status" not in st.session_state:
    st.session_state.fan_status= ""

if "pump_status" not in st.session_state:
    st.session_state.pump_status= ""
    
if "fan_status_list" not in st.session_state:
    st.session_state.fan_status_list=[]

if "pump_status_list" not in st.session_state:
    st.session_state.pump_status_list=[]
    
if "temperatura_estufa_list" not in st.session_state:
    st.session_state.temperatura_estufa_list= [0]
    
if "umidade_estufa_list" not in st.session_state:
    st.session_state.umidade_estufa_list= [0]
    
if "nivel_agua_estufa_list" not in st.session_state:
    st.session_state.nivel_agua_estufa_list= [0]

if "N_list" not in st.session_state:
    st.session_state.N_list= [0]
    
if "P_list" not in st.session_state:
    st.session_state.P_list= [0]

if "K_list" not in st.session_state:
    st.session_state.K_list= [0]
    
if "temperatura_estufa_delta" not in st.session_state:
    st.session_state.temperatura_estufa_delta= ""
    
if "umidade_estufa_delta" not in st.session_state:
    st.session_state.umidade_estufa_delta= ""
    
if "nivel_agua_estufa_delta" not in st.session_state:
    st.session_state.nivel_agua_estufa_delta= ""

if "N_delta" not in st.session_state:
    st.session_state.N_delta= ""
    
if "P_delta" not in st.session_state:
    st.session_state.P_delta= ""

if "K_delta" not in st.session_state:
    st.session_state.K_delta= ""
    
if 'new_row' not in st.session_state:
    st.session_state.new_row= ""
    
if 'pump_prob' not in st.session_state:
    st.session_state.pump_prob= ""
    
if 'fan_prob' not in st.session_state:
    st.session_state.fan_prob= ""
    
if st.session_state.data_hoje == None:
    
    # Inicializa as informações de data e hora
    st.session_state.data_hoje = sis.returnData()
    st.session_state.dia_semana = sis.DiadaSemana()
    st.session_state.hora  = datetime.now()
    
    #Inicializa as informações atuais do tempo
    response=sis.getWeatherNow(LATITUDE, LONGITUDE, TOKEN)
    icon, st.session_state.tmed_hoje, st.session_state.tmin_hoje, st.session_state.tmax_hoje, st.session_state.umidade_hoje, st.session_state.vento_hoje= sis.getWeatherNow_information(response)
    st.session_state.icon_hoje= sis.get_Icon(icon)
    st.session_state.hoje_desc= sis.get_weather_description(icon)
    st.session_state.tmin_hoje_list.append(st.session_state.tmin_hoje)
    st.session_state.tmax_hoje_list.append(st.session_state.tmax_hoje)
    st.session_state.tmed_hoje_list.append(st.session_state.tmed_hoje)
    st.session_state.umidade_hoje_list.append(st.session_state.umidade_hoje)
    st.session_state.vento_hoje_list.append(st.session_state.vento_hoje)
    st.session_state.tmin_hoje_delta = np.round((st.session_state.tmin_hoje_list[-1] - st.session_state.tmin_hoje_list[-2]), 2)
    st.session_state.tmax_hoje_delta = np.round((st.session_state.tmax_hoje_list[-1] - st.session_state.tmax_hoje_list[-2]), 2)
    st.session_state.tmed_hoje_delta = np.round((st.session_state.tmed_hoje_list[-1] - st.session_state.tmed_hoje_list[-2]), 2)
    st.session_state.umidade_hoje_delta = np.round((st.session_state.umidade_hoje_list[-1] - st.session_state.umidade_hoje_list[-2]), 2)
    st.session_state.vento_hoje_delta = np.round((st.session_state.vento_hoje_list[-1] - st.session_state.vento_hoje_list[-2]), 2)
     
    #Inicializa as informações da predição do tempo
    response = sis.getWeatherPrediction(LATITUDE, LONGITUDE, TOKEN, fh=54)
    st.session_state.previsao_tempo = sis.getWeatherPrediction_information(response)
    
    # Inicializa as informações dos sensores da estufa 
    st.session_state.new_dataset, st.session_state.contador, st.session_state.N, st.session_state.P, st.session_state.K, st.session_state.temperatura_estufa, st.session_state.umidade_estufa, st.session_state.nivel_agua_estufa, st.session_state.pump_status, st.session_state.fan_status, st.session_state.new_row= sis.simulate_sensor_data(st.session_state.dataset, st.session_state.new_dataset, st.session_state.contador)
    st.session_state.temperatura_estufa_list.append(st.session_state.temperatura_estufa)
    st.session_state.umidade_estufa_list.append(st.session_state.umidade_estufa)
    st.session_state.nivel_agua_estufa_list.append(st.session_state.nivel_agua_estufa)
    st.session_state.N_list.append(st.session_state.N)
    st.session_state.P_list.append(st.session_state.P)
    st.session_state.K_list.append(st.session_state.K)
    st.session_state.temperatura_estufa_delta= np.round((st.session_state.temperatura_estufa_list[-1] - st.session_state.temperatura_estufa_list[-2]), 2)
    st.session_state.umidade_estufa_delta= np.round((st.session_state.umidade_estufa_list[-1] - st.session_state.temperatura_estufa_list[-2]), 2)
    st.session_state.nivel_agua_estufa_delta= np.round((st.session_state.nivel_agua_estufa_list[-1] - st.session_state.nivel_agua_estufa_list[-2]), 2)
    st.session_state.N_delta= np.round((st.session_state.N_list[-1] - st.session_state.N_list[-2]), 2)
    st.session_state.P_delta= np.round((st.session_state.P_list[-1] - st.session_state.P_list[-2]), 2)
    st.session_state.K_delta= np.round((st.session_state.K_list[-1] - st.session_state.K_list[-2]), 2)
    st.session_state.fan_status= ""
    st.session_state.pump_status= ""
    if st.session_state.fan_status == 1.0:
        st.session_state.fan_status_list.append(1)
    
    if st.session_state.pump_status == 1.0:
        st.session_state.pump_status_list.append(1)
    
    st.session_state.pump_prob=  sis.return_pump_prob(st.session_state.new_row)
    st.session_state.fan_prob= sis.return_fan_prob(st.session_state.new_row)




st.markdown(
    """
    <h1 style='text-align: center;'>
        Smart Irrigation System
    </h1>
    """, 
    unsafe_allow_html=True
)

st.write(' ')
st.write(' ')
st.write(' ')
st.write(' ')
st.write(' ')
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Clima", "Estufa", "Adubação" ,"Dashboard", "Database"])
with tab1:
    
    with st.container():
        st.markdown(
    f"""
    <h2 style='text-align: left;'>
        {st.session_state.dia_semana}, {st.session_state.data_hoje} 
    </h2>
    """, 
    unsafe_allow_html=True
    )
    # Função para incrementar 1 segundo
    
    st.session_state.hora= datetime.now()      
    st.markdown(
            f"""
            <h3 style='text-align: left;'>
            {st.session_state.hora.strftime("%H:%M")}
            </h3>
        """, 
        unsafe_allow_html=True
        )
        
    # Primeira divisão horizontal
    with st.container():
        # Divisão vertical dentro da última divisão horizontal
        col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
        with col1:
            subcoll21, subcoll22, subcoll23= st.columns(3)
            with subcoll22:
                st.title(f'{st.session_state.icon_hoje}')        
                st.markdown(
                    f"""
                    <h4 style='text-align: left;'>
                    {st.session_state.hoje_desc}
                    </h4>
                """, 
                unsafe_allow_html=True)
        

        with col2:
            dia_semana = list(st.session_state.previsao_tempo[0].keys())[0]
    
            st.session_state.dia_1 = dia_semana
            st.session_state.data_1 = st.session_state.previsao_tempo[0][dia_semana].get('data')
            icon_ = st.session_state.previsao_tempo[0][dia_semana].get('icon')
            st.session_state.icon_1 = sis.get_Icon(icon_)
            st.session_state.tmin_1 = st.session_state.previsao_tempo[0][dia_semana].get('temp_min')
            st.session_state.tmax_1 = st.session_state.previsao_tempo[0][dia_semana].get('temp_max')
            
            st.markdown(
                f"""
                <h5 style='text-align: center;'>
                {st.session_state.dia_1}
                </h5>
                """, 
                unsafe_allow_html=True
                )
            st.markdown(
                f"""
                <h5 style='text-align: center;'>
                    {st.session_state.data_1}
                </h5>
                """, 
                unsafe_allow_html=True
                )

            # Layout com texto estilizado
            col21, col22, col23 = st.columns(3)    
            with col22:

                st.write(f'{st.session_state.icon_1}')
            
            col211, col212, = st.columns(2)
            with col211:
                st.markdown(
                """
                <style>
                .small-text {
                    font-size: 14px         
                }
                </style>
                """,
                unsafe_allow_html=True
                )#color: #555;

                # Aplicando estilo menor para min e max
                st.markdown(f'<div class="small-text">min {st.session_state.tmin_1}ºC </div>', unsafe_allow_html=True)
            
            with col212:
                st.markdown(
                """
                <style>
                .small-text {
                    font-size: 14px         
                }
                </style>
                """,
                unsafe_allow_html=True
            )#color: #555;

                # Aplicando estilo menor para min e max
                st.markdown(f'<div class="small-text">max {st.session_state.tmax_1}ºC </div>', unsafe_allow_html=True)


        with col3:
            dia_semana = list(st.session_state.previsao_tempo[1].keys())[0]
    
            st.session_state.dia_2 = dia_semana
            st.session_state.data_2 = st.session_state.previsao_tempo[1][dia_semana].get('data')
            icon_ = st.session_state.previsao_tempo[1][dia_semana].get('icon')
            st.session_state.icon_2 = sis.get_Icon(icon_)
            st.session_state.tmin_2 = st.session_state.previsao_tempo[1][dia_semana].get('temp_min')
            st.session_state.tmax_2 = st.session_state.previsao_tempo[1][dia_semana].get('temp_max')
        # Layout com texto estilizado
            st.markdown(
            f"""
            <h5 style='text-align: center;'>
                {st.session_state.dia_2}
            </h5>
            """, 
            unsafe_allow_html=True
            )
            
            st.markdown(
            f"""
            <h5 style='text-align: center;'>
                {st.session_state.data_2}
            </h5>
            """, 
            unsafe_allow_html=True
            )
            
            
            col31, col32, col33 = st.columns(3)
            
            with col32:
                st.write(f'{st.session_state.icon_2}')
            
            col311, col312, = st.columns(2)
            with col311:
                st.markdown(
                """
                <style>
                .small-text {
                    font-size: 14px         
                }
                </style>
                """,
                unsafe_allow_html=True
                )#color: #555;

                # Aplicando estilo menor para min e max
                st.markdown(f'<div class="small-text">min {st.session_state.tmin_2}ºC </div>', unsafe_allow_html=True)
            
            with col312:
                st.markdown(
                """
                <style>
                .small-text {
                    font-size: 14px         
                }
                </style>
                """,
                unsafe_allow_html=True
            )#color: #555;

                # Aplicando estilo menor para min e max
                st.markdown(f'<div class="small-text">max {st.session_state.tmax_2}ºC </div>', unsafe_allow_html=True)


        with col4:
            dia_semana = list(st.session_state.previsao_tempo[2].keys())[0]
    
            st.session_state.dia_3 = dia_semana
            st.session_state.data_3 = st.session_state.previsao_tempo[2][dia_semana].get('data')
            icon_ = st.session_state.previsao_tempo[2][dia_semana].get('icon')
            st.session_state.icon_3 = sis.get_Icon(icon_)
            st.session_state.tmin_3 = st.session_state.previsao_tempo[2][dia_semana].get('temp_min')
            st.session_state.tmax_3 = st.session_state.previsao_tempo[2][dia_semana].get('temp_max')
            # Layout com texto estilizado
            st.markdown(
            f"""
            <h5 style='text-align: center;'>
                {st.session_state.dia_3}
            </h5>
            """, 
            unsafe_allow_html=True
            )
            st.markdown(
            f"""
            <h5 style='text-align: center;'>
                {st.session_state.data_3}
            </h5>
            """, 
            unsafe_allow_html=True
            )
            
            
            col41, col42, col43 = st.columns(3)
            
            with col42:
                st.write(f'{st.session_state.icon_3}')
            
            col411, col412, = st.columns(2)
            with col411:
                st.markdown(
                """
                <style>
                .small-text {
                    font-size: 14px         
                }
                </style>
                """,
                unsafe_allow_html=True
                )#color: #555;

                # Aplicando estilo menor para min e max
                st.markdown(f'<div class="small-text">min {st.session_state.tmin_3}ºC </div>', unsafe_allow_html=True)
            
            with col412:
                st.markdown(
                """
                <style>
                .small-text {
                    font-size: 14px         
                }
                </style>
                """,
                unsafe_allow_html=True
            )#color: #555;

                # Aplicando estilo menor para min e max
                st.markdown(f'<div class="small-text">max {st.session_state.tmax_3}ºC </div>', unsafe_allow_html=True)
        
        with col5:
            dia_semana = list(st.session_state.previsao_tempo[3].keys())[0]
            st.session_state.dia_4 = dia_semana
            st.session_state.data_4 = st.session_state.previsao_tempo[3][dia_semana].get('data')
            icon_ = st.session_state.previsao_tempo[3][dia_semana].get('icon')
            st.session_state.icon_4 = sis.get_Icon(icon_)
            st.session_state.tmin_4 = st.session_state.previsao_tempo[3][dia_semana].get('temp_min')
            st.session_state.tmax_4 = st.session_state.previsao_tempo[3][dia_semana].get('temp_max')
        # Layout com texto estilizado
            st.markdown(
            f"""
            <h5 style='text-align: center;'>
                {st.session_state.dia_4}
            </h5>
            """, 
            unsafe_allow_html=True
            )
            st.markdown(
            f"""
            <h5 style='text-align: center;'>
               {st.session_state.data_4}
            </h5>
            """, 
            unsafe_allow_html=True
            )
            
            
            col51, col52, col53 = st.columns(3)
            
            with col52:
                st.write(f'{st.session_state.icon_4}')
            
            col511, col512, = st.columns(2)
            with col511:
                st.markdown(
                """
                <style>
                .small-text {
                    font-size: 14px         
                }
                </style>
                """,
                unsafe_allow_html=True
                )#color: #555;

                # Aplicando estilo menor para min e max
                st.markdown(f'<div class="small-text">min {st.session_state.tmin_4}ºC </div>', unsafe_allow_html=True)
            
            with col512:
                st.markdown(
                """
                <style>
                .small-text {
                    font-size: 14px         
                }
                </style>
                """,
                unsafe_allow_html=True
            )#color: #555;

                # Aplicando estilo menor para min e max
                st.markdown(f'<div class="small-text">max {st.session_state.tmax_4}ºC </div>', unsafe_allow_html=True)


        with col6:
            dia_semana = list(st.session_state.previsao_tempo[4].keys())[0]
            st.session_state.dia_5 = dia_semana
            st.session_state.data_5 = st.session_state.previsao_tempo[4][dia_semana].get('data')
            icon_ = st.session_state.previsao_tempo[4][dia_semana].get('icon')
            st.session_state.icon_5 = sis.get_Icon(icon_)
            st.session_state.tmin_5 = st.session_state.previsao_tempo[4][dia_semana].get('temp_min')
            st.session_state.tmax_5 = st.session_state.previsao_tempo[4][dia_semana].get('temp_max')
            # Layout com texto estilizado
            st.markdown(
            f"""
            <h5 style='text-align: center;'>
                {st.session_state.dia_5}
            </h5>
            """, 
            unsafe_allow_html=True
            )
            st.markdown(
            f"""
            <h5 style='text-align: center;'>
                {st.session_state.data_5}
            </h5>
            """, 
            unsafe_allow_html=True
            )
            
            
            col61, col62, col63 = st.columns(3)
            
            with col62:
                st.write(f'{st.session_state.icon_5}')
            
            col561, col562, = st.columns(2)
            with col561:
                st.markdown(
                """
                <style>
                .small-text {
                    font-size: 14px         
                }
                </style>
                """,
                unsafe_allow_html=True
                )#color: #555;

                # Aplicando estilo menor para min e max
                st.markdown(f'<div class="small-text">min {st.session_state.tmin_5}ºC </div>', unsafe_allow_html=True)
            
            with col562:
                st.markdown(
                """
                <style>
                .small-text {
                    font-size: 14px         
                }
                </style>
                """,
                unsafe_allow_html=True
            )#color: #555;

                # Aplicando estilo menor para min e max
                st.markdown(f'<div class="small-text">max {st.session_state.tmax_5}ºC </div>', unsafe_allow_html=True)


        with col7:
            dia_semana = list(st.session_state.previsao_tempo[5].keys())[0]
            st.session_state.dia_6 = dia_semana
            st.session_state.data_6 = st.session_state.previsao_tempo[5][dia_semana].get('data')
            icon_ = st.session_state.previsao_tempo[5][dia_semana].get('icon')
            st.session_state.icon_6 = sis.get_Icon(icon_)
            st.session_state.tmin_6 = st.session_state.previsao_tempo[5][dia_semana].get('temp_min')
            st.session_state.tmax_6 = st.session_state.previsao_tempo[5][dia_semana].get('temp_max')
            # Layout com texto estilizado
            st.markdown(
            f"""
            <h5 style='text-align: center;'>
                {st.session_state.dia_6}
            </h5>
            """, 
            unsafe_allow_html=True
            )
            st.markdown(
            f"""
            <h5 style='text-align: center;'>
                {st.session_state.data_6}
            </h5>
            """, 
            unsafe_allow_html=True
            )
            
            
            col71, col72, col73 = st.columns(3)
            
            with col72:
                st.write(f'{st.session_state.icon_6}')
            col711, col712, = st.columns(2)
            with col711:
                st.markdown(
                """
                <style>
                .small-text {
                    font-size: 14px         
                }
                </style>
                """,
                unsafe_allow_html=True
                )#color: #555;

                # Aplicando estilo menor para min e max
                st.markdown(f'<div class="small-text">min {st.session_state.tmin_6}ºC </div>', unsafe_allow_html=True)
            
            with col712:
                st.markdown(
                """
                <style>
                .small-text {
                    font-size: 14px         
                }
                </style>
                """,
                unsafe_allow_html=True
            )#color: #555;

                # Aplicando estilo menor para min e max
                st.markdown(f'<div class="small-text">max {st.session_state.tmax_6}ºC </div>', unsafe_allow_html=True)



    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')

    with st.container():
        # Divisão vertical dentro da última divisão horizontal
        subcol21, subcol22, subcol23, subcol24, subcol25, subcol26, subcol27= st.columns(7)
        
        with subcol21:
            subcoll21, subcoll22, subcoll23= st.columns(3)
            with subcoll22:
                st.title(' ')        
                st.markdown(
                    """
                    <h4 style='text-align: left;'>
                    
                    </h4>
                """, 
                unsafe_allow_html=True)

        with subcol22:
            st.metric(label="Temperatura", value=f"{st.session_state.tmed_hoje} °C", delta=f"{st.session_state.tmed_hoje_delta} °C")
        
        with subcol23:
   
            st.metric(label="Temperatura Mínima", value=f"{st.session_state.tmin_hoje} °C", delta=f"{st.session_state.tmin_hoje_delta} °C")
            
        with subcol24:

            st.metric(label="Temperatura Máxima", value=f"{st.session_state.tmax_hoje} °C", delta=f"{st.session_state.tmax_hoje_delta} °C")     
            
        with subcol25:

            st.metric(label="Umidade", value=f"{st.session_state.umidade_hoje} %", delta=f"{st.session_state.umidade_hoje_delta} %")
            
        with subcol26:
            st.metric(label="Velocidade do vento", value=f"{st.session_state.vento_hoje} km/h", delta=f"{st.session_state.vento_hoje_delta} km/h")
        
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    
    # Primeira divisão horizontal
    with st.container():
        # Divisão vertical dentro da última divisão horizontal
        subcol11, subcol12 = st.columns(2)
            
        with subcol11:
            st.markdown(
                f"""
                <h3 style='text-align: left;'>
                {CIDADE}-{ESTADO}
                </h3 >
                """, 
                unsafe_allow_html=True
            )
            subc1, subc2, subc3, subc4= st.columns(4)
            with subc1:
                st.markdown(
                f"""
                <h8 style='text-align: left;'>
                Lat: {LATITUDE} S
                </h8 >
                """, 
                unsafe_allow_html=True
            )
                
            with subc2:
                st.markdown(
                f"""
                <h8 style='text-align: left;'>
                Lon: {LONGITUDE} O
                </h8 >
                """, 
                unsafe_allow_html=True
            )

    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    # Coordenadas da localização
    latitude = -21.67583
    longitude = -50.32667

    # Criar DataFrame com a localização
    df = pd.DataFrame(
        [{"lat": latitude, "lon": longitude}]
    )

    # Configurar camada do mapa
    layer = pdk.Layer(
        "ScatterplotLayer",
        data=df,
        get_position="[lon, lat]",
        get_color="[255, 0, 0, 160]",  # Cor do ponto (vermelho)
        get_radius=200,  # Raio do ponto
    )

    # Configurar visualização inicial do mapa
    view_state = pdk.ViewState(
        latitude=latitude,
        longitude=longitude,
        zoom=15,
        pitch=0,
    )

    # Configuração do mapa com estilo de terreno
    terrain_map = pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        map_style="mapbox://styles/mapbox/satellite-v9" #"mapbox://styles/mapbox/outdoors-v11",  # Estilo de terreno
    )

    # Exibir o mapa no Streamlit
    # st.pydeck_chart(terrain_map)
    map_deck = st.pydeck_chart(terrain_map)


    if st.button('Recentralizar'):
        st.rerun()  # Isso força o "reload" do script


 
with tab2:
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')

    with st.container():

        subcol11, subcol12, subcol13, subcol14, subcol15, subcol16= st.columns(6)
        with subcol11:
            st.markdown(
            f"""
            <h2 style='text-align: left;'>
                {st.session_state.dia_semana}, {st.session_state.data_hoje} 
            </h2>
            """, 
            unsafe_allow_html=True
            )
            st.session_state.hora= datetime.now()      
            st.markdown(
                f"""
                <h3 style='text-align: left;'>
                {st.session_state.hora.strftime("%H:%M")}
                </h3>
                """, 
                unsafe_allow_html=True
                )
    
            
            # Função para incrementar 1 segundo
        with subcol13:

            st.write(' ')
            st.write(' ')
            st.write(' ')
            st.metric(label="Temperatura", value=f"{st.session_state.temperatura_estufa} °C", delta=f"{st.session_state.temperatura_estufa_delta}°C")  
            
        with subcol14:

            st.write(' ')
            st.write(' ')
            st.write(' ')
            st.metric(label="Umidade", value=f"{st.session_state.umidade_estufa} %", delta=f"{st.session_state.umidade_estufa_delta} %")
            
        with subcol15:

            st.write(' ')
            st.write(' ')
            st.write(' ')
            st.metric(label="Nivel de Agua", value=f"{st.session_state.nivel_agua_estufa} mm", delta=f"{st.session_state.nivel_agua_estufa_delta} mm")
    
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    
    # Coluna da direita (com 2 divisões horizontais)

       
    # Segunda divisão horizontal
    with st.container():
        # Divisão vertical dentro da última divisão horizontal
        subcol31, subcol32= st.columns(2)
        with subcol31:
            # Divisão vertical dentro da última divisão horizontal

            
            st.markdown(
                    """
                    <h3 style='text-align: center;'>
                     Pump status:
                    </h3>
                    """, 
                    unsafe_allow_html=True
                )
            
            st.write(' ')
            st.write(' ')
            st.write(' ')  
            
            
            if st.session_state.pump_status == 1.0:
                st.markdown(
                    """
                    <h1 style='text-align: center;color:#0A7E31'>
                        On
                    </h1>
                    """, 
                    unsafe_allow_html=True
                )
            
            else:
                st.markdown(
                        """
                        <h1 style='text-align: center;color:#6a040f'>
                            Off
                        </h1>
                        """, 
                        unsafe_allow_html=True
                    )
                
            st.write(' ')
            st.write(' ')
            st.write(' ')
            st.write(' ')
            st.write(' ')
            st.write(' ')
            
            st.markdown(
                    """
                    <h4 style='text-align: center;'>
                        Probabilidade de Ligar a Bomba
                    </h4>
                    """, 
                    unsafe_allow_html=True
                )
            
            st.write(' ')
            st.write(' ')
            st.write(' ')
           

            st.markdown(
                    f"""
                    <h1 style='text-align: center;'>
                       {st.session_state.pump_prob} %
                    </h1>
                    """, 
                    unsafe_allow_html=True
                )
            
   
        with subcol32:
             
            
            st.markdown(
                    """
                    <h3 style='text-align: center;'>
                    Fan status:
                    </h3>
                    """, 
                    unsafe_allow_html=True
                )
            
            st.write(' ')
            st.write(' ')
            st.write(' ')
            if st.session_state.fan_status == 1.0:
                st.markdown(
                        """
                        <h1 style='text-align: center;color:#0A7E31'>
                            On
                        </h1>
                        """, 
                        unsafe_allow_html=True
                    )
            else:
                st.markdown(
                        """
                        <h1 style='text-align: center;color:#6a040f'>
                            Off
                        </h1>
                        """, 
                        unsafe_allow_html=True
                    )
            
            st.write(' ')
            st.write(' ')
            st.write(' ')
            st.write(' ')
            st.write(' ')
            st.write(' ')
            st.markdown(
                    """
                    <h3 style='text-align: center;'>
                        Probabilidade de Ligar a Fan
                    </h3>
                    """, 
                    unsafe_allow_html=True
                )
            st.write(' ')
            st.write(' ')
            st.write(' ')
            
            st.markdown(
                    f"""
                    <h1 style='text-align: center;'>
                       {st.session_state.fan_prob} %
                    </h1>
                    """, 
                    unsafe_allow_html=True
                )
 
with tab3:

    st.markdown(
    """
    <h2 style='text-align: center;'>
        Nível de Nutrientes
    </h2>
    """, 
    unsafe_allow_html=True
    ) 
    st.write(' ')
    st.write(' ')
    st.write(' ')
    # Primeira divisão horizontal

    with st.container():
        # Divisão vertical dentro da última divisão horizontal
        subcol21, subcol22, subcol23, subcol24, subcol25, subcol26, subcol27= st.columns(7)
        with subcol22:
            st.metric(label="N", value=f"{st.session_state.N}", delta=f"{st.session_state.N_delta}")  
            
        with subcol24:
            st.metric(label="P", value=f"{st.session_state.P}", delta=f"{st.session_state.P_delta}") 
            
        with subcol26:
            st.metric(label="K", value=f"{st.session_state.K}", delta=f"{st.session_state.K_delta}")
        
        subcol221, subcol222, subcol223= st.columns(3)
        with subcol222:
            # Dados
            data = {
                'Variáveis': ['N 255', 'P 255', 'K 255'],
                'Valores': [st.session_state.N, st.session_state.P, st.session_state.K],
            }

            df_nutrientes = pd.DataFrame(data)
            # Exibir o gráfico
            fig = sis.plot_radar(df_nutrientes)
            #st.pyplot(fig)
            # Mostrar o gráfico no Streamlit
            st.plotly_chart(fig, key='radar nutrientes')    
with tab4:
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')   
  
    with st.container():
        # Divisão vertical dentro da última divisão horizontal
        subcol311, subcol312, subcol313, subcol314, subcol315= st.columns(5)
        with subcol312:
            st.markdown(
                    f"""
                    <h3 style='text-align: center;'>
                    Pump On
                    </h3>
                    """, 
                    unsafe_allow_html=True
                )
            
            subcol321, subcol322, subcol323= st.columns(3)
            with subcol322:
                st.metric(label="  ", value=f"{len(st.session_state.pump_status_list)}")
                
        with subcol314:
            st.markdown(
                    f"""
                    <h3 style='text-align: center;'>
                     Fan On
                    </h3>
                    """, 
                    unsafe_allow_html=True
                )
            
            subcol331, subcol332, subcol333= st.columns(3)
            with subcol332:
                st.metric(label="  ", value=f"{len(st.session_state.fan_status_list)}")
    # Primeira divisão horizontal
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    
    with st.container():        
        subcol411, subcol412 = st.columns(2)
        with subcol411:
            st.markdown(
                """
                <h2 style='text-align: center;'>
                    Temperatura
                </h2>
                """, 
                unsafe_allow_html=True
            )
            #st.pyplot(generate_plot(data, 'x', 'y'))
            # Gerar o gráfico 
            fig = sis.generate_plot(st.session_state.new_dataset, 'data', 'temperatura')
            st.plotly_chart(fig, key='temperatura')
            
            with subcol412:
                st.markdown(
                    """
                    <h2 style='text-align: center;'>
                        Umidade
                    </h2>
                    """, 
                    unsafe_allow_html=True
                )
                #st.pyplot(generate_plot(data, 'x', 'y'))
                # Gerar o gráfico 
                fig = sis.generate_plot(st.session_state.new_dataset, 'data', 'umidade')
                st.plotly_chart(fig, key='umidade')
                  
                
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    
    with st.container():
        subcol421, subcol422 = st.columns(2)
        with subcol421:
            st.markdown(
                    """
                    <h2 style='text-align: center;'>
                        Nível de água
                    </h2>
                    """, 
                    unsafe_allow_html=True
                )  
            #st.pyplot(generate_plot(data, 'x', 'y'))
            # Gerar o gráfico 
            fig = sis.generate_plot(st.session_state.new_dataset, 'data', 'nivel de agua')
            st.plotly_chart(fig, key='nivel de agua')


with tab5:
    st.dataframe(st.session_state.new_dataset)          

st.session_state.data_hoje = sis.returnData()
st.session_state.dia_semana = sis.DiadaSemana()
st.session_state.dia_1 = list(st.session_state.previsao_tempo[0].keys())[0]

if st.session_state.dia_semana == st.session_state.dia_1:
    response = sis.getWeatherPrediction(LATITUDE, LONGITUDE, TOKEN, fh=54)
    st.session_state.previsao_tempo = sis.getWeatherPrediction_information(response)


def time_estufa(): 
    new_dataset, i, N, P, K, tempreature, humidity, water_level, pump_status, fan_status, new_row= sis.simulate_sensor_data(st.session_state.dataset, st.session_state.new_dataset, st.session_state.contador)
    time.sleep(15) #300
    print('OK')
    return new_dataset, i, N, P, K, tempreature, humidity, water_level, pump_status, fan_status, new_row

if st.session_state.contador > st.session_state.new_dataset.shape[0]:
    st.session_state.contador=0 
    
# Inicializa as informações dos sensores da estufa 
st.session_state.new_dataset, st.session_state.contador, st.session_state.N, st.session_state.P, st.session_state.K, st.session_state.temperatura_estufa, st.session_state.umidade_estufa, st.session_state.nivel_agua_estufa, st.session_state.pump_status, st.session_state.fan_status,st.session_state.new_row= time_estufa()
st.session_state.temperatura_estufa_list.append(st.session_state.temperatura_estufa)
st.session_state.umidade_estufa_list.append(st.session_state.umidade_estufa)
st.session_state.nivel_agua_estufa_list.append(st.session_state.nivel_agua_estufa)
st.session_state.N_list.append(st.session_state.N)
st.session_state.P_list.append(st.session_state.P)
st.session_state.K_list.append(st.session_state.K)
st.session_state.temperatura_estufa_delta= np.round((st.session_state.temperatura_estufa_list[-1] - st.session_state.temperatura_estufa_list[-2]), 2)
st.session_state.umidade_estufa_delta= np.round((st.session_state.umidade_estufa_list[-1] - st.session_state.umidade_estufa_list[-2]), 2)
st.session_state.nivel_agua_estufa_delta= np.round((st.session_state.nivel_agua_estufa_list[-1] - st.session_state.nivel_agua_estufa_list[-2]), 2)
st.session_state.N_delta= np.round((st.session_state.N_list[-1] - st.session_state.N_list[-2]), 2)
st.session_state.P_delta= np.round((st.session_state.P_list[-1] - st.session_state.P_list[-2]), 2)
st.session_state.K_delta= np.round((st.session_state.K_list[-1] - st.session_state.K_list[-2]), 2)

if st.session_state.fan_status == 1.0:
    st.session_state.fan_status_list.append(1)

if st.session_state.pump_status == 1.0:
    st.session_state.pump_status_list.append(1)

st.session_state.pump_prob=  sis.return_pump_prob(st.session_state.new_row)
st.session_state.fan_prob= sis.return_fan_prob(st.session_state.new_row)    

print(st.session_state.pump_prob==0.0)

def time_weather():
    LATITUDE= -21.6
    LONGITUDE= -50.3
    TOKEN='4970da017dd95b5934d38c4a0559aa29'
    # Pausar por 10 minutos --> 600 segundos
    response=sis.getWeatherNow(LATITUDE, LONGITUDE, TOKEN)
    icon, temperatura,temp_min, temp_max, umidade, vento_vel= sis.getWeatherNow_information(response)
    icon_=sis.get_Icon(icon)
    description = sis.get_weather_description(icon)
    print('OK')
    return temperatura,temp_min, temp_max, umidade, vento_vel, icon_, description

if st.session_state.contador % 20 == 0:
    st.session_state.tmed_hoje, st.session_state.tmin_hoje, st.session_state.tmax_hoje, st.session_state.umidade_hoje, st.session_state.vento_hoje,st.session_state.icon_hoje, st.session_state.hoje_desc= time_weather()
    st.session_state.tmin_hoje_list.append(st.session_state.tmin_hoje)
    st.session_state.tmax_hoje_list.append(st.session_state.tmax_hoje)
    st.session_state.tmed_hoje_list.append(st.session_state.tmed_hoje)
    st.session_state.umidade_hoje_list.append(st.session_state.umidade_hoje)
    st.session_state.vento_hoje_list.append(st.session_state.vento_hoje)

    st.session_state.tmin_hoje_delta = np.round((st.session_state.tmin_hoje_list[-1] - st.session_state.tmin_hoje_list[-2]), 2)
    st.session_state.tmax_hoje_delta = np.round((st.session_state.tmax_hoje_list[-1] - st.session_state.tmax_hoje_list[-2]), 2)
    st.session_state.tmed_hoje_delta = np.round((st.session_state.tmed_hoje_list[-1] - st.session_state.tmed_hoje_list[-2]), 2)
    st.session_state.umidade_hoje_delta = np.round((st.session_state.umidade_hoje_list[-1] - st.session_state.umidade_hoje_list[-2]), 2)
    st.session_state.vento_hoje_delta = np.round((st.session_state.vento_hoje_list[-1] - st.session_state.vento_hoje_list[-2]), 2)

time_()

# with st.sidebar:
#     st.title('Menu')