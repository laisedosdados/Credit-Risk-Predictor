## **Credit Risk Predictor**
## Visão geral do projeto
O objetivo do **Credit Risk Predictor** é simular o ciclo completo de análise de risco de crédito. No projeto, o comportamento financeiro do cliente será analisado e, a partir disso, será criado um modelo preditivo a fim de identificar a probabilidade de inadimplência de novos clientes.
## Stacks utilizadas
**1. Linguagem**: Python   
**2. Bibliotecas de dados**: Pandas, SQLAlchemy, psycopg2   
**3. Banco de Dados**: PostgreSQL  
**4. Machine learning**: Scikit-Learn   
**5. Visualização de dados**: Matplotlib e Seaborn
## Objetivos
* Identificar quais clientes tem maior possibilidade de inadimplência;
* Criar indicadores que auxiliem na tomda de decisão;
* Simular anonimização de dados sensíveis;
## Etapas:
1. **Simulação com dados fictícios (Python)**:  `Pandas`e `Numpy` serão utilizados para criar um dataset com 1000 clientes fictícios.
2. **Carregamento de dados (PostgreSQL)**: os dados serão carregados em um banco de dados relacional e a integridade será garantida através de chaves primárias e estrangeiras.
3. **Feature Engineering (SQL)**: criação de visões analíticas para calcular métricas de risco (taxa de atraso, média de gastos, score, etc);
4. **Modelagem Preditiva (Machine Learning):** Os dados preparados por SQL serão utilizados para treinar um modelo de classificação em Python;
