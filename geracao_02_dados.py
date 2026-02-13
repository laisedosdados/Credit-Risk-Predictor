# CRIANDO O SCRIPT PARA CONECTAR OS DADOS AO RENDER
# Importando as bibliotecas 
import panda as pd
from sqlalchemy import create_engine #biblioteca para banco de dados
conexao_render = 'postgresql://credit_risk_predictor_user:0NGyB02EsoZWw4mRes8TwEo1WBbi5psV@dpg-d676ubjuibrs73cf3t4g-a.oregon-postgres.render.com/credit_risk_predictor'
# Conectando ao banco de dados
def carregar_dados():
    try:
        print("Tentando conectar o Python ao PostgreSQL no Render...")
        engine = create_engine(conexao_render)


