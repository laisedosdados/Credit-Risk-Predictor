# Importando as bibliotecas necessárias
import pandas as pd
import numpy as np
import os
# Gerando os números aleatórios
np.random.seed(42)
numero_clientes = 1000
# Criando o dataframe com os dados dos clientes
dados_clientes = {
    'id_cliente': range(1, numero_clientes + 1),
    'renda_mensal': range(4500, 1500, numero_clientes).clip(1621),
    'score_interno': np.random.randint(300, 1000, numero_clientes),
    'estado_civil': np.random.choice(['Solteiro', 'Casado', 'Divorciado', 'Viúvo'], numero_clientes)
}
df_clientes = pd.DataFrame(dados_clientes)
# Criando a tabela de faturas
faturas = []
# Para cada id de cliente vou gerar uma fatura:
for c_id in range(1, numero_clientes + 1):
    score = df_clientes[df_clientes['id_cliente'] == c_id]['score_interno'].values[0]
probabilidade_atraso = 0.30 if score < 500 else 0.05
# Gerando 6 meses de histórico para o cliente específico
for mes in range(1,7):
   pago_em_dia = np.random.choice([0,1]), p=[probabilidade_atraso, 1 - probabilidade_atraso] 
   # Criando as faturas
   faturas.append({
       'id_cliente': c_id,
       'mes_referencia': mes,
       'valot_fatura': np.random.uniform(200, 5000),
       'pago_em_dia': pago_em_dia
   })