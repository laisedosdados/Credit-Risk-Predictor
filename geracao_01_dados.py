# Importando as bibliotecas necessárias
import pandas as pd
import numpy as np
import os
# Gerando os números aleatórios
numero_clientes = 1000
np.random.seed(42)
# Criando o dataframe com os dados dos clientes
dados_clientes = {
    'id_cliente': range(1, numero_clientes + 1),
    'renda_mensal': np.random.normal(4500, 1500, numero_clientes).clip(1621),
    'score_interno': np.random.randint(300, 1000, numero_clientes), #sorteia uma nota de 300 a mil para cada
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
        pago_em_dia = np.random.choice([0,1], p=[probabilidade_atraso, 1 - probabilidade_atraso]) 
        # Criando as faturas
        faturas.append({
            'id_cliente': c_id,
            'mes_referencia': mes,
            'valor_fatura': np.random.uniform(200, 5000),
            'pago_em_dia': pago_em_dia
        })
# Transformando as faturas em um Dataframe
df_faturas = pd.DataFrame(faturas)
# Salvando os arquivos
caminho_raw = 'data/raw'
# Se a pasta não existir, ela é criada
if not os.path.exists(caminho_raw):
    os.makedirs(caminho_raw)
# Salvando a tabela de clientes e faturas em formato CSV
# O index = false evita criar uma coluna com números desnecessários
df_clientes.to_csv(f"{caminho_raw}/clientes.csv", index=False)
df_faturas.to_csv(f"{caminho_raw}/faturas.csv", index=False)
# Imprimindo na tela
print(f"Foram gerados {len(df_clientes)} clientes e {len(df_faturas)} faturas!!!")
print(f"Verifique agora a pasta: {caminho_raw}")