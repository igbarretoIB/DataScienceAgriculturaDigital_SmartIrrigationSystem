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

# Configurar layout da página como wide
st.set_page_config(layout="wide")

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
tab1, tab2, tab3, tab4 = st.tabs(["Clima", "Estufa", "Adubação" ,"Dashboard"])
with tab1:
    # Primeira divisão horizontal
    with st.container():
        # Divisão vertical dentro da última divisão horizontal
        subcol11, subcol12 = st.columns(2)
            
        with subcol11:
            st.markdown(
                """
                <h3 style='text-align: left;'>
                Luiziânia-SP
                </h3 >
                """, 
                unsafe_allow_html=True
            )
            subc1, subc2, subc3, subc4= st.columns(4)
            with subc1:
                st.markdown(
                """
                <h8 style='text-align: left;'>
                Lat: 21º40'33" S
                </h8 >
                """, 
                unsafe_allow_html=True
            )
                
            with subc2:
                st.markdown(
                """
                <h8 style='text-align: left;'>
                Lon: 50º19'36 O
                </h8 >
                """, 
                unsafe_allow_html=True
            )

    st.write(' ')
    st.write(' ')
    st.write(' ')
    with st.container():
        # Divisão vertical dentro da última divisão horizontal
        col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
        with col1:
            # Layout com texto estilizado
            st.markdown(
            """
            <h5 style='text-align: center;'>
                Segunda
            </h5>
            """, 
            unsafe_allow_html=True
            )
            st.markdown(
            """
            <h5 style='text-align: center;'>
                01/10
            </h5>
            """, 
            unsafe_allow_html=True
            )
            
            
            col11, col12, col13 = st.columns(3)
            
            with col12:
                st.write(':sunny:')
            
            col111, col112, = st.columns(2)
            with col111:
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
                st.markdown('<div class="small-text">min 20ºC </div>', unsafe_allow_html=True)
            
            with col112:
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
                st.markdown('<div class="small-text">max 30ºC </div>', unsafe_allow_html=True)


        with col2:
            # Layout com texto estilizado
            st.markdown(
            """
            <h5 style='text-align: center;'>
                Terça
            </h5>
            """, 
            unsafe_allow_html=True
            )
            st.markdown(
            """
            <h5 style='text-align: center;'>
                02/10
            </h5>
            """, 
            unsafe_allow_html=True
            )
            
            
            col21, col22, col23 = st.columns(3)
            
            with col22:
                st.write(':sunny:')
            
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
                st.markdown('<div class="small-text">min 20ºC </div>', unsafe_allow_html=True)
            
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
                st.markdown('<div class="small-text">max 30ºC </div>', unsafe_allow_html=True)


        with col3:
        # Layout com texto estilizado
            st.markdown(
            """
            <h5 style='text-align: center;'>
                Quarta
            </h5>
            """, 
            unsafe_allow_html=True
            )
            st.markdown(
            """
            <h5 style='text-align: center;'>
                03/10
            </h5>
            """, 
            unsafe_allow_html=True
            )
            
            
            col31, col32, col33 = st.columns(3)
            
            with col32:
                st.write(':partly_sunny:')
            
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
                st.markdown('<div class="small-text">min 20ºC </div>', unsafe_allow_html=True)
            
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
                st.markdown('<div class="small-text">max 30ºC </div>', unsafe_allow_html=True)


        with col4:
            # Layout com texto estilizado
            st.markdown(
            """
            <h5 style='text-align: center;'>
                Quinta
            </h5>
            """, 
            unsafe_allow_html=True
            )
            st.markdown(
            """
            <h5 style='text-align: center;'>
                04/10
            </h5>
            """, 
            unsafe_allow_html=True
            )
            
            
            col41, col42, col43 = st.columns(3)
            
            with col42:
                st.write(':partly_sunny:')
            
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
                st.markdown('<div class="small-text">min 20ºC </div>', unsafe_allow_html=True)
            
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
                st.markdown('<div class="small-text">max 30ºC </div>', unsafe_allow_html=True)
        
        with col5:
        # Layout com texto estilizado
            st.markdown(
            """
            <h5 style='text-align: center;'>
                Sexta
            </h5>
            """, 
            unsafe_allow_html=True
            )
            st.markdown(
            """
            <h5 style='text-align: center;'>
                05/10
            </h5>
            """, 
            unsafe_allow_html=True
            )
            
            
            col51, col52, col53 = st.columns(3)
            
            with col52:
                st.write(':rain_cloud:')
            
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
                st.markdown('<div class="small-text">min 20ºC </div>', unsafe_allow_html=True)
            
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
                st.markdown('<div class="small-text">max 30ºC </div>', unsafe_allow_html=True)


        with col6:
            # Layout com texto estilizado
            st.markdown(
            """
            <h5 style='text-align: center;'>
                Sábado
            </h5>
            """, 
            unsafe_allow_html=True
            )
            st.markdown(
            """
            <h5 style='text-align: center;'>
                06/10
            </h5>
            """, 
            unsafe_allow_html=True
            )
            
            
            col61, col62, col63 = st.columns(3)
            
            with col62:
                st.write(':rain_cloud:')
            
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
                st.markdown('<div class="small-text">min 20ºC </div>', unsafe_allow_html=True)
            
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
                st.markdown('<div class="small-text">max 30ºC </div>', unsafe_allow_html=True)


        with col7:
            # Layout com texto estilizado
            st.markdown(
            """
            <h5 style='text-align: center;'>
                Domingo
            </h5>
            """, 
            unsafe_allow_html=True
            )
            st.markdown(
            """
            <h5 style='text-align: center;'>
                07/10
            </h5>
            """, 
            unsafe_allow_html=True
            )
            
            
            col71, col72, col73 = st.columns(3)
            
            with col72:
                st.write(':thunder_cloud_and_rain:')
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
                st.markdown('<div class="small-text">min 20ºC </div>', unsafe_allow_html=True)
            
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
                st.markdown('<div class="small-text">max 30ºC </div>', unsafe_allow_html=True)



    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    # Criar colunas
    col1, col2 = st.columns(2)

    # Coluna da esquerda (com 3 divisões horizontais)
    with col1: 
        st.markdown(
        """
        <h2 style='text-align: left;'>
            Agora
        </h2>
        """, 
        unsafe_allow_html=True
        )
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.markdown(
        """
        <h5 style='text-align: left;'>
            Quarta-feira, 11/12/2024
        </h5>
        """, 
        unsafe_allow_html=True
        )
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')

        # Primeira divisão horizontal
        with st.container():
            # Divisão vertical dentro da última divisão horizontal
            subcol21, subcol22, subcol23= st.columns(3)
            
            with subcol21:
                st.metric(label="Temperatura", value="30 °C", delta="1.2 °C")  
                
            with subcol22:
                st.metric(label="Umidade", value="80 %", delta="10 %")
                
            with subcol23:
                st.metric(label="Velocidade do vento", value="10 km", delta="5 km")
        
    st.write(' ')
    st.write(' ')
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


    # # Coordenadas da localização
    # latitude = -21.67583
    # longitude = -50.32667

    # m = folium.Map(
    #     location=[latitude, longitude], 
    #     zoom_start=10, 
    #     tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', 
    #     attr='Esri'
    # )

    # # Adicionar um marcador
    # folium.Marker(
    #     [latitude, longitude],
    #     popup="Minha localização",
    #     icon=folium.Icon(color="red", icon="info-sign"),
    # ).add_to(m)

    # # Exibir o mapa no Streamlit
    # st.title("Mapa Integrado com Folium")
    # st_folium(m, width=1200, height=500)

with tab2:
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')

    st.markdown(
    """
    <h2 style='text-align: center;'>
        Agora
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
        subcol11, subcol12, subcol13, subcol14, subcol15, subcol16, subcol17 = st.columns(7)
        with subcol13:
            st.metric(label="Temperatura", value="30 °C", delta="1.2 °C")  
            
        with subcol14:
            st.metric(label="Umidade", value="80 %", delta="10 %")
            
        with subcol15:
            st.metric(label="Nivel de Agua", value="100 mm", delta="100 mm")
    
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
                    """
                    <h1 style='text-align: center;'>
                       50 %
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
                     Pump status:
                    </h3>
                    """, 
                    unsafe_allow_html=True
                )
            
            
            # st.markdown(
            #         """
            #         <h3 style='text-align: center;>
            #            Pump status:
            #         </h3>
            #         """, 
            #         unsafe_allow_html=True
            #     )
            
            st.write(' ')
            st.write(' ')
            st.write(' ')  
            st.markdown(
                    """
                    <h1 style='text-align: center;color:#0A7E31'>
                        On
                    </h1>
                    """, 
                    unsafe_allow_html=True
                )
            
        with subcol32:
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
                    """
                    <h1 style='text-align: center;'>
                       70 %
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
                    Fan status:
                    </h3>
                    """, 
                    unsafe_allow_html=True
                )
            
            st.write(' ')
            st.write(' ')
            st.write(' ')  
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
            st.metric(label="N", value="255", delta="10")  
            
        with subcol24:
            st.metric(label="P", value="255", delta="10")
            
        with subcol26:
            st.metric(label="K", value="255", delta="10")
        
        subcol221, subcol222, subcol223= st.columns(3)
        with subcol222:
            # Função para criar o gráfico de radar
            # def plot_radar(data):
            #     # Preparar dados
            #     labels = data['Variáveis'].tolist()
            #     valores = data['Valores'].tolist()
            #     max_valores = [255] * len(labels)

            #     # Fechar os polígonos
            #     valores += valores[:1]
            #     max_valores += max_valores[:1]

            #     # Ângulos para cada variável
            #     angulos = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
            #     angulos += angulos[:1]

            #     # Criar o gráfico
            #     fig, ax = plt.subplots(figsize=(5, 5), subplot_kw={'projection': 'polar'})
            #     fig.patch.set_facecolor("#0D1117")
            #     # Traçar o triângulo maior (máximos)
            #     ax.plot(angulos, max_valores, color="gray", linewidth=1.5, linestyle="--", label="Máximo")

            #     # Traçar o triângulo menor (valores reais)
            #     ax.fill(angulos, valores, color="#0A7E31", alpha=0.25, label="Valores Reais")
            #     ax.plot(angulos, valores, color="#0A7E31", linewidth=2)

            #     # Estilo do gráfico
            #     ax.set_facecolor("#0D1117")  # Fundo branco
            #     #ax.set_facecolor((1, 1, 1, 0))  # Fundo transparente (sem preenchimento)
            #     #ax.grid(color="gray", linestyle="--", linewidth=0.5)
            #     ax.spines['polar'].set_visible(False)  # Remover borda externa
            #     ax.set_yticks([])  # Remover rótulos dos círculos

            #     # Adicionar rótulos das variáveis
            #     ax.set_xticks(angulos[:-1])
            #     ax.set_xticklabels(labels, fontsize=12, color="white")


            #     return fig

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
                                  width=500, # Aumentar a largura da área de plotagem 
                                  height=500 # Aumentar a altura da área de plotagem 
                                  ) 
                return fig
            
            # Dados
            data = {
                'Variáveis': ['N 255', 'P 255', 'K 255'],
                'Valores': [120, 180, 150],
            }

            df = pd.DataFrame(data)
            # Exibir o gráfico
            fig = plot_radar(df)
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
    # Gerar gráficos de exemplo
    # def generate_plot(data, x, y):
    #     fig, ax = plt.subplots()
    #     fig.patch.set_facecolor("#0D1117")
        
    #     sns.lineplot(data=data, x=x, y=y, ax=ax, color='green')
        
    #     ax.set_facecolor("#0D1117")
    #     # ax.set_title(title, color='white')
    #     ax.tick_params(colors='white')
    #     ax.xaxis.label.set_color('white')
    #     ax.yaxis.label.set_color('white')
        
    #     return fig
    
    def generate_plot(data, x, y):
        fig = px.line(data, x=x, y=y, title='Gráfico de Linhas', line_shape='linear') #
        fig.update_traces(line=dict(color='green'), mode='lines+markers')
        #fig.update_traces(line=dict(color='#0A7E31', mode='lines+markers'))
        fig.update_layout( plot_bgcolor='#0D1117', paper_bgcolor='#0D1117', font_color='white' ) 
        return fig
    
    data = pd.DataFrame({ 'x': range(10), 'y': [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] })
    
    
    with st.container():
        # Divisão vertical dentro da última divisão horizontal
        subcol311, subcol312, subcol313, subcol314, subcol315= st.columns(5)
        with subcol312:
            st.markdown(
                    """
                    <h3 style='text-align: center;'>
                    Pump On count
                    </h3>
                    """, 
                    unsafe_allow_html=True
                )
            
            subcol321, subcol322, subcol323= st.columns(3)
            with subcol322:
                st.metric(label="  ", value="35")
                
        with subcol314:
            st.markdown(
                    """
                    <h3 style='text-align: center;'>
                    Fan On count
                    </h3>
                    """, 
                    unsafe_allow_html=True
                )
            
            subcol331, subcol332, subcol333= st.columns(3)
            with subcol332:
                st.metric(label="  ", value="35")
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
            fig = generate_plot(data, 'x', 'y')
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
                fig = generate_plot(data, 'x', 'y')
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
            fig = generate_plot(data, 'x', 'y')
            st.plotly_chart(fig, key='nivel de agua')
            
with st.sidebar:
    st.title('Menu')
