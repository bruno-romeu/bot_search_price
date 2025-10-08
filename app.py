import pandas as pd
import streamlit as st
from selenium import webdriver
from main import search_amazon
from streamlit_option_menu import option_menu

with st.sidebar:
    '''
    Configurações do menu lateral do app
    '''
    selected = option_menu("Products Scraper", ["Página Inicial", "Visualização de Dados", '---', 'Settings'], 
        icons=['house', 'bar-chart', 'gear'], menu_icon="search", default_index=0,
        styles= {
            "container": {"width": "300px!important"},
            "nav-link-selected": {"background-color": "#2124c5ff"}
        }
        )
    selected
#======================================================================================================================================

st.title("Products Scraper")

if 'results' not in st.session_state:
    st.session_state.results = None

def get_driver():
    if 'driver' not in st.session_state:
        st.write('Iniciando o WebDriver...')
        options = webdriver.EdgeOptions()
        options.add_argument('--headless')
        st.session_state.driver = webdriver.Edge(options=options)
    return st.session_state.driver

def quit_driver():
    if 'driver' in st.session_state:
        st.session_state.driver.quit()
        del st.session_state.driver
        st.success('WebDriver encerrado.')


st.header('Faça sua busca')
user_input = st.text_input("Qual produto você deseja pesquisar na Amazon?", label_visibility="collapsed")
col1, col2 = st.columns([3, 1])

with col1:
    if st.button("Pesquisar", use_container_width=True):
        driver = get_driver()
        with st.spinner("Buscando produtos..."):
            st.session_state.results = search_amazon(driver, user_input)

with col2:
    if st.button("Encerrar WebDriver", use_container_width=True):
        quit_driver()

if st.session_state.results is not None:
    if not st.session_state.results:
        st.warning("Nenhum resultado encontrado para a sua busca.")
    else:
        st.success(f"Encontramos {len(st.session_state.results)} resultados!")
        df = pd.DataFrame(st.session_state.results)
        st.dataframe(df)

        st.header("Resultados Detalhados:")
        for index, row in df.iterrows():
            st.subheader(row['titulo_produto'])
            col_preco, col_link = st.columns(2)
            with col_preco:
                st.metric(label="Preço", value=f"R$ {row['preco']}")
            with col_link:
                st.markdown(f"[Ver na loja]({row['link']})")
            st.divider()
