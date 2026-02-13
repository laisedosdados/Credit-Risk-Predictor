import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
load_dotenv()
conexao_render = os.environ.get('DATABASE_URL')
def carregar_dados():
    try:
        print("Tentando conectar o Python ao PostgreSQL no Render...")
        engine = create_engine(conexao_render)  
        with engine.connect() as conn:
            print("Conexao estabelecida com sucesso!!")      
        print("Lendo os arquivos CSV...")
        df_clientes = pd.read_csv('data/raw/clientes.csv')
        df_faturas = pd.read_csv('data/raw/faturas.csv')   
        print("Enviando dados para o PostgreSQL...")
        df_clientes.to_sql('clientes', engine, if_exists='replace', index=False)
        df_faturas.to_sql('faturas', engine, if_exists='replace', index=False)   
        print("Seus dados ja estao na nuvem!!!")    
    except Exception as e:
        print(f"Erro: {e}")
if __name__ == "__main__":
    carregar_dados()