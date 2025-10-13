import pandas as pd
import os 

def load_and_prepare_data(filepath):
    if not os.path.exists(filepath):
        return pd.DataFrame()

    df = pd.read_csv(filepath)
    df['termo_busca'] = df['termo_busca'].str.strip()
    df['data_hora_busca'] = pd.to_datetime(df['data_hora_busca'])
    df['preco_numerico'] = pd.to_numeric(df['preco'].str.replace('.', '', regex=False).str.replace(',', '.'), errors='coerce')
    
    return df

