import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Carregando o dataset
df = pd.read_excel('dataset_1.xlsx')

# Verificando as primeiras linhas do dataset
df.head()

# Verificando as informações do dataset
df.info()

# Verificando a presença de dados faltantes
df.isnull().sum()
# exibe a quantidade e as colunas com dados faltantes
print(df.isnull().sum())

# Removendo colunas que não serão utilizadas na análise
df = df.drop(['Patient addmited to semi-intensive unit (1=yes, 0=no)',
             'Patient addmited to regular ward (1=yes, 0=no)'], axis=1)

# Verificando a distribuição dos dados
df.describe()

# Verificando a presença de outliers
# Para verificar a presença de outliers na coluna no excell, vamos utilizar um boxplot ou um histograma
sns.boxplot(x=df['Patient age quantile'])
plt.show()

# verificar a presença de valores únicos em cada coluna
for coluna in df.columns:
    print(coluna)
    print(df[coluna].unique())

# Exportando o dataset tratado
# df.to_excel('dataset_tratado.xlsx')
