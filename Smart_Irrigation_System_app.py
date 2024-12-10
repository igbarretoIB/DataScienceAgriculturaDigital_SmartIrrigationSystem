import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pydeck as pdk
import folium
from streamlit_folium import st_folium

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
tab1, tab2, tab3 = st.tabs(["Clima", "Estufa", "Dashboard"])
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
        with subcol23:
            st.metric(label="N", value="255", delta="10")  
            
        with subcol24:
            st.metric(label="P", value="255", delta="10")
            
        with subcol25:
            st.metric(label="K", value="255", delta="10")
    
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
            
    
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
            st.write(' ')
            st.write(' ')
            st.write(' ')
            st.markdown(
                    """
                    <h4 style='text-align: center;'>
                        Pump On/ Pump Off
                    </h4>
                    """, 
                    unsafe_allow_html=True
                )
    
        with subcol32:
            st.markdown(
                    """
                    <h4 style='text-align: center;'>
                        Probabilidade de Ligar a Fan
                    </h4>
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
                        Fan On/ Fan Off
                    </h4>
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
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')   
    # Gerar gráficos de exemplo
    def generate_plot(title):
        fig, ax = plt.subplots()
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        ax.plot(x, y)
        ax.set_title(title)
        return fig
    
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.markdown(
    """
    <h2 style='text-align: center;'>
        Temperatura
    </h2>
    """, 
    unsafe_allow_html=True
    )
    
    # Primeira divisão horizontal
    with st.container():
        st.pyplot(generate_plot("Gráfico 1"))
        
    st.write(' ')
    st.write(' ')
    st.write(' ')
    
    st.markdown(
    """
    <h2 style='text-align: center;'>
        Umidade
    </h2>
    """, 
    unsafe_allow_html=True
    )  
    # Segunda divisão horizontal
    with st.container():
        st.pyplot(generate_plot("Gráfico 2"))
    
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.markdown(
    """
    <h2 style='text-align: center;'>
        Nível de água
    </h2>
    """, 
    unsafe_allow_html=True
    )  
    # Terceira divisão horizontal
    with st.container():
        st.pyplot(generate_plot("Gráfico 3"))
    
with st.sidebar:
    st.title('Menu')
