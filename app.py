import streamlit as st
import pandas as pd
import joblib
# Carregando o modelo de IA criado
modelo = joblib.load('modelo_risco_credito.pkl')
# Desenhando a tela do site
st.title('🏦 Previsão de Risco de Crédito')
st.write('Simulador de Inteligência Artificial para aprovação de clientes.')
st.markdown('---')
# Criando as caixinhas para o usuário digitar os dados
col1, col2 = st.columns(2)
with col1:
    renda = st.number_input('Renda Mensal (R$)', min_value=0.0, value=5000.0)
    fatura = st.number_input('Valor da Fatura (R$)', min_value=0.0, value=1500.0)
with col2:
    score = st.number_input('Score Interno (0 a 1000)', min_value=0, max_value=1000, value=600)
    estado_civil = st.selectbox('Estado Civil', ['Solteiro', 'Casado', 'Divorciado', 'Viúvo'])
# Criando o botão para a IA analisar o risco do cliente
if st.button('🔮 Analisar Risco do Cliente'):
    # Preparando o one-hot enconding
    dados = {
        'renda_mensal': [renda],
        'score_interno': [score],
        'valor_fatura': [fatura],
        'estado_civil_Casado': [1 if estado_civil == 'Casado' else 0],
        'estado_civil_Divorciado': [1 if estado_civil == 'Divorciado' else 0],
        'estado_civil_Solteiro': [1 if estado_civil == 'Solteiro' else 0],
        'estado_civil_Viúvo': [1 if estado_civil == 'Viúvo' else 0]
    }
    # Criando a tabela de 1 linha para a IA ler
    df_cliente = pd.DataFrame(dados)
    # Fazendo a previsão
    previsao = modelo.predict(df_cliente)[0]
    st.markdown('---')
    # Mostrando o resultado na tela com cores
    if previsao == 1:
        st.success('✅ **CLIENTE APROVADO!** O modelo indica que este cliente pagará em dia.')
    else:
        st.error('🚨 **ALERTA DE RISCO!** O modelo indica alta chance de calote (inadimplência).')