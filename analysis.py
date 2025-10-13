import pandas as pd

df_read = pd.read_csv('data/analise_produtos.csv')

df_read['preco_numerico'] = pd.to_numeric(df_read['preco'].str.replace('.', '', regex=False).str.replace(',', '.'), errors='coerce')

df_read['data_hora_busca'] = pd.to_datetime(df_read['data_hora_busca'])

df_pivot = df_read.pivot(index='data_hora_busca', columns='loja', values='preco_numerico')


