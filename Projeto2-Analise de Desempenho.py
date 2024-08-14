import pandas as pd

# Carregar dados
df = pd.read_csv('desempenho.csv')

# Exibir as primeiras linhas do dataframe
print("Primeiras linhas do dataframe:")
print(df.head())

# Verificar informações gerais do dataframe
print("\nInformações do dataframe:")
print(df.info())

# Verificar estatísticas descritivas apenas para colunas numéricas
print("\nEstatísticas descritivas:")
print(df[['nota_matematica', 'nota_portugues']].describe())

# Verificar valores nulos
print("\nValores nulos:")
print(df.isnull().sum())

# Média das notas apenas para colunas numéricas
media_notas = df[['nota_matematica', 'nota_portugues']].mean()
print("\nMédia das notas:")
print(media_notas)

# Correlação entre notas de Matemática e Português
correlacao = df[['nota_matematica', 'nota_portugues']].corr()
print("\nCorrelação entre notas de Matemática e Português:")
print(correlacao)

import matplotlib.pyplot as plt
import seaborn as sns

# Configurar o estilo dos gráficos
sns.set(style='whitegrid')

# Gráfico de notas de Matemática e Português
plt.figure(figsize=(10, 5))
sns.scatterplot(data=df, x='nota_matematica', y='nota_portugues')
plt.title('Notas de Matemática vs Português')
plt.xlabel('Nota em Matemática')
plt.ylabel('Nota em Português')
plt.show()

# Gráfico de médias das notas
plt.figure(figsize=(8, 6))
df[['nota_matematica', 'nota_portugues']].mean().plot(kind='bar')
plt.title('Média das Notas')
plt.xlabel('Disciplina')
plt.ylabel('Nota Média')
plt.show()
