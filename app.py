import pandas as pd
import streamlit as st
from selenium import webdriver
from scraper import search_amazon
from streamlit_option_menu import option_menu
from analysis import load_and_prepare_data

with st.sidebar:
    
    #Configurações do menu lateral do app
    
    selected = option_menu("Products Scraper", ["Página Inicial", "Visualização de Dados", '---', 'Settings'], 
        icons=['house', 'bar-chart', 'gear'], menu_icon="search", default_index=0,
        styles= {
            "container": {"width": "300px!important"},
            "nav-link-selected": {"background-color": "#2124c5ff"}
        }
        )
#===============================================================================================================================================================

# Se selecionado 'Página Inicial' no menu lateral, renderiza o código a seguir (por padrão, é renderizado também caso nada tenha sido escolhido no menu)
if selected == "Página Inicial":
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
                clean_term = user_input.strip()
                st.session_state.results = search_amazon(driver, clean_term)

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


# Se selecionado 'Visualização de Dados' no menu lateral, renderiza o código a seguir:
elif selected == "Visualização de Dados":
    st.title("Análise de variação de preço")

    df_read = load_and_prepare_data('data/analise_produtos.csv')
    if df_read.empty:
        st.warning("Nenhum dado encontrado. Faça uma busca na 'Página Inicial' primeiro.")
    else:
        col1, col2 = st.columns(2)
        min_date = df_read['data_hora_busca'].min().date()
        max_date = df_read['data_hora_busca'].max().date()


        with col1:
            start_date = st.date_input("Data de Início: ", min_date)
        with col2:
            final_date = st.date_input("Data Final: ", max_date)

        
        terms = df_read['termo_busca'].unique()
        selected_term = st.selectbox(   
            "Selecione um termo de busca",
            terms,
        )
        filtered_df = df_read[
            (df_read['termo_busca'] == selected_term) &
            (df_read['data_hora_busca'].dt.date >= start_date) & 
            (df_read['data_hora_busca'].dt.date <= final_date)
            ]
        st.divider()
        
        try:
            if not filtered_df.empty:
                df_pivot = filtered_df.pivot(
                    index='data_hora_busca', 
                    columns='loja', 
                    values='preco_numerico'
                )

                st.subheader("Evolução do Preço Médio Encontrado")
                df_date = filtered_df.set_index('data_hora_busca')
                df_resampled = df_date.groupby('loja')['preco_numerico'].resample('D').mean()
                df_final = df_resampled.unstack(level='loja')
                df_preenchido = df_final.ffill()
                st.line_chart(df_preenchido)
                
                st.write("Dados Filtrados:")
                st.dataframe(filtered_df)

            else:
                st.warning("Nenhum dado encontrado para os filtros selecionados.")
        except Exception as e:
            st.error("erro ao buscar dados dos produtos ")
