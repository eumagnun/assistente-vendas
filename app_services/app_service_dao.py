
import pandas as pd
import altair as alt

def get_data():
    df = pd.read_csv('./app_data/dados_vendas_carros.csv')

    print(df.to_string()) 
    return df