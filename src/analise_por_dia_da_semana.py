import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
dados = pd.read_csv('../data/tips_traduzido.csv', sep=';')

# Distribuição entre o dia da semana e o valor total da conta
sns.catplot(x='dia_da_semana',y='valor_total_conta', data=dados)
# Distribuição entre o valor total da conta e o valor da gorjeta com coloração diferente para cada dia da semana.
sns.relplot(x='valor_total_conta', y='valor_gorjeta', hue='dia_da_semana', data=dados)
# Distribuição entre o valor total da conta e a porcentagem da gorjeta com coloração diferente para cada
# dia da semana.
sns.relplot(x='valor_total_conta', y='porcentagem', hue='dia_da_semana', data=dados)
# Distribuição entre o valor total da conta e o valor da gorjeta gerando um gráfico para cada dia da semana.
sns.relplot(x='valor_total_conta', y='valor_gorjeta', hue='dia_da_semana', col='dia_da_semana', data=dados)
# Distribuição entre o valor total da conta e a porcentagem da gorjeta gerando um gráfico para cada dia da semana.
sns.relplot(x='valor_total_conta', y='porcentagem', hue='dia_da_semana', col='dia_da_semana', data=dados)
# Distribuição entre o valor total da conta e a porcentagem da gorjeta gerando um gráfico para cada dia da semana.
# Aqui porém, será traçada uma linha.
sns.lmplot(x='valor_total_conta', y='porcentagem', hue='dia_da_semana', col='dia_da_semana', data=dados)
plt.show()
