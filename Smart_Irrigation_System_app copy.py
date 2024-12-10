import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

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
with st.container():
    # Divisão vertical dentro da última divisão horizontal
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    with col1:
        st.subheader('Seg')
        st.write('01/10')
        st.write(':sunny:')
        st.write('min 20ºC')
        st.write('max 30ºC')


    with col2:
        st.subheader('Ter')
        st.write('02/10')
        st.write(':sunny:')
        st.write('min 20ºC')
        st.write('max 30ºC')

    with col3:
        st.subheader('Qua')
        st.write('03/10')
        st.write(':partly_sunny:')
        st.write('min 20ºC')
        st.write('max 30ºC')

    with col4:
        st.subheader('Qui')
        st.write('04/10')
        st.write(':partly_sunny:')
        st.write('min 20ºC')
        st.write('max 30ºC')
    with col5:
        st.subheader('Sex')
        st.write('05/10')
        st.write(':rain_cloud:')
        st.write('min 20ºC')
        st.write('max 30ºC')


    with col6:
        st.subheader('Sab')
        st.write('06/10')
        st.write(':rain_cloud:')
        st.write('min 20ºC')
        st.write('max 30ºC')


    with col7:
        st.subheader('Dom')
        st.write('07/10')
        st.write(':thunder_cloud_and_rain:')
        st.write('min 20ºC')
        st.write('max 30ºC')

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

# Criar colunas
col1, col2 = st.columns(2)

# Coluna da esquerda (com 3 divisões horizontais)
with col1: 
    st.markdown(
    """
    <h2 style='text-align: center;'>
        Agora
    </h2>
    """, 
    unsafe_allow_html=True
    )
    # Primeira divisão horizontal
    with st.container():
        # Divisão vertical dentro da última divisão horizontal
        subcol11, subcol12, subcol13= st.columns(3)
        with subcol11:
            st.metric(label="Temperatura", value="30 °C", delta="1.2 °C")  
            
        with subcol12:
            st.metric(label="Umidade", value="80 %", delta="10 %")
            
        with subcol13:
            st.metric(label="Nivel de Agua", value="100 mm", delta="100 mm")
    
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

# Coluna da direita (com 2 divisões horizontais)
with col2:
    st.markdown(
    """
    <h2 style='text-align: center;'>
        Nível de Nutrientes
    </h2>
    """, 
    unsafe_allow_html=True
    ) 
    
    # Primeira divisão horizontal
    with st.container():
        # Divisão vertical dentro da última divisão horizontal
        subcol21, subcol22, subcol23= st.columns(3)
        with subcol21:
            st.metric(label="N", value="255", delta="10")  
            
        with subcol22:
            st.metric(label="P", value="255", delta="10")
            
        with subcol23:
            st.metric(label="K", value="255", delta="10")
    
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

with st.sidebar:
    colt1, colt2, colt3 = st.columns(3)
    with colt2:
        st.subheader('Clima APP')
        st.write(' ')


    st.title('Menu')
