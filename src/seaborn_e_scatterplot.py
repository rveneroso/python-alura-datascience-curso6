import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
dados = pd.read_csv('../data/tips_traduzido.csv', sep=';')

# Gerando o gráfico de distribuição valor da conta X valor da gorjeta.
# ATENÇÃO!!!!!!!!!!!!! Esse gráfico só funcionou ao explicitar a forma de obtenção das colunas 'valor_da_conta'
# e 'valor_gorjeta' por seus índices numéricos. Não sei o que há de diferente nesse DataFrame mas por alguma
# razão, não está sendo possível recuperar as colunas por seus nomes.
sns.scatterplot(x = dados.iloc[:,0], y = dados.iloc[:,1], data = dados)
plt.show()

dados['porcentagem'] = (dados.iloc[:,0] / dados.iloc[:,1]).round(2)
# Gerando o gráfico de distribuição valor da conta X porcentagem da gorjeta
sns.scatterplot(x = dados.iloc[:,0], y = dados.iloc[:,-1], data = dados)
plt.show()

# Gerando o gráfico de linha valor da conta X porcentagem da gorjeta
sns.relplot(x = dados.iloc[:,0], y = dados.iloc[:,-1], kind='line', data = dados)
plt.show()

sns.lmplot(x='valor_total_conta', y='porcentagem', data=dados)
plt.show()


