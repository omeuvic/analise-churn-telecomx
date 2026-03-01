# %% [markdown]
# #📌 Extracão

# %%
import pandas as pd

# URL github alura
url = 'https://raw.githubusercontent.com/ingridcristh/challenge2-data-science/main/TelecomX_Data.json'
df = pd.read_json(url)
df = pd.json_normalize(df.to_dict(orient='records'))

print(df.head())

# %% [markdown]
# #🔧 Transformação

# %%
# Substituir começo dos titulos

df.columns = df.columns.str.replace('customer.', '', regex=False)
df.columns = df.columns.str.replace('account.', '', regex=False)
df.columns = df.columns.str.replace('internet.', '', regex=False)
df.columns = df.columns.str.replace('Charges.', '', regex=False)

df.head()


# %%
# Há Clientes Duplicados
df[df['customerID'].duplicated()]
df = df.drop_duplicates(subset='customerID')
print(f"Total de customerID duplicados: {df['customerID'].duplicated().sum()}")


# Há Clientes sem Informações no Churn
nulos = df['Churn'].isnull().sum()
vazios = (df['Churn'] == '').sum()

print(f"Valores nulos no Churn: {nulos}")
print(f"Valores vazios no Churn: {vazios}")


# %%
# Corrigindo digitação
df['Churn'] = df['Churn'].str.lower()
df['gender'] = df['gender'].str.lower()
df['Partner'] = df['Partner'].str.lower()
df['Dependents'] = df['Dependents'].str.lower()


# Remover espaços se tiver
df['Churn'] = df['Churn'].str.replace(' ', '')
df['gender'] = df['gender'].str.replace(' ', '')
df['Partner'] = df['Partner'].str.replace(' ', '')
df['Dependents'] = df['Dependents'].str.replace(' ', '')

# yes por 1 e no por 0
df['Churn'] = df['Churn'].replace({'yes': 1, 'no': 0})
df['gender'] = df['gender'].replace({'yes': 1, 'no': 0})
df['Partner'] = df['Partner'].replace({'yes': 1, 'no': 0})
df['Dependents'] = df['Dependents'].replace({'yes': 1, 'no': 0})

# %% [markdown]
# #📊 Carga e análise

# %%
# Análise Descritiva

df.describe()

# %%
# Distribuição da Evasão
import matplotlib.pyplot as plt
import seaborn as sns

# Grafico com a Evasão de clientes pela variável'Churn'
sns.countplot(x='Churn', data=df)

# Adicionando título e exibindo o gráfico
plt.title('Quantidade de Evasão de Clientes')
plt.legend(title='1 = Ficou, 0 = saiu')
plt.show()

# %%
#Contagem de Evasão por Variáveis Categóricas
sns.countplot(x='Contract', hue='Churn', data=df)

# Adicionando título e exibindo o gráfico
plt.title('Quantidade de Clientes por Tipo de Contrato')
plt.show()

# %%
# Contagem de Evasão por Variáveis Numéricas

sns.boxplot(x='Churn', y='Monthly', data=df)

plt.title('Total Gasto por Evasão')
plt.xlabel('Churn')
plt.ylabel('Monthly')

plt.show()

# %% [markdown]
# #📄Relatorio Final

# %% [markdown]
# Análise de Churn da Telecom X
# 
# ## Introdução
# O objetivo deste projeto foi analisar os dados de clientes da Telecom X para identificar fatores relacionados à evasão de clientes (churn). Essa análise é importante para entender o comportamento dos clientes e ajudar a empresa a criar estratégias para melhorar a retenção.
# 
# ## Limpeza e Preparação dos Dados
# Os dados foram carregados a partir de um arquivo JSON e normalizados para facilitar a análise. Foram realizadas etapas de limpeza, como remoção de clientes duplicados, padronização de textos e conversão da variável Churn para formato numérico (0 para clientes que permaneceram e 1 para clientes que cancelaram). Essas etapas garantiram maior consistência e qualidade dos dados.
# 
# ## Análise Exploratória e Insights
# A análise mostrou que clientes com contrato mensal apresentam maior taxa de evasão em comparação com contratos de longo prazo. Também foi possível observar que os valores mensais possuem relação com o churn, indicando que o custo pode influenciar na decisão do cliente de cancelar o serviço.
# 
# ## Conclusões e Recomendações
# Conclui-se que o tipo de contrato é um dos principais fatores que influenciam a evasão. Clientes com contratos mensais apresentam maior risco de cancelamento. Como recomendação, a empresa pode incentivar contratos de longo prazo, oferecer benefícios para fidelização e monitorar clientes com maior risco de evasão. Essas ações podem ajudar a reduzir o churn e melhorar a retenção de clientes.


