# CRIANDO O SCRIPT PARA CONECTAR OS DADOS AO RENDER
# Importando as bibliotecas 
import pandas as pd
from sqlalchemy import create_engine #biblioteca para banco de dados
import os
from dotenv import load_dotenv
load_dotenv() # Isso aqui lê o arquivo .env que você acabou de criar
conexao_render = os.environ.get('DATABASE_URL')
# Conectando ao banco de dados
def carregar_dados():
    try:
        print("Tentando conectar o Python ao PostgreSQL no Render...")
        engine = create_engine(conexao_render)
        # Testando a conexão
        with engine.connect() as conn:
            print("Conexão estabelecida com sucesso!!")
        # Lendo os arquivos CSVs de clientes e faturas
        print("Lendo os arquivos CSV...")
        df_clientes = pd.read_csv('data/raw/clientes.csv')
        df_faturas = pd.read_csv('data/raw/faturas.csv')
        print("Arquvos lidos com sucesso!!!")
        # Enviando tudo para o banco de dados
        print("Enviando a tabela clientes para o PostgreSQL...")
        df_clientes.to_sql('clientes', engine, if_exists='replace', index=False)
        print("Enviando a tabela faturas para o PostgreSQL...")
        df_faturas.to_sql('faturas', engine, if_exists='replace', index=False)
        print("Seus dados já estão na nuvem, agora você pode usá-los!!!")
    except Exception as e:
        print("Erro:{}".format(e))
if __name__ == "__main__":
    carregar_dados()
              
              


