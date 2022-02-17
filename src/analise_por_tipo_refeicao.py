import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
dados = pd.read_csv('../data/tips_traduzido.csv', sep=';')

#sns.catplot(x='tipo_refeicao', y='valor_total_conta',data=dados)
# Gera um gráfico semelhante ao anterior mas separa um pouco mais os pontos que indicam contas de mesmo valor
#sns.catplot(x='tipo_refeicao', y='valor_total_conta',kind='swarm', data=dados)
# Gera um gráfico do estilo violino.
# sns.violinplot(x='tipo_refeicao', y='valor_total_conta', data=dados)
#sns.boxplot(x='tipo_refeicao', y='valor_total_conta', data=dados)

contas_almoco = dados.query("tipo_refeicao == 'Almoço'").valor_total_conta
contas_jantar = dados.query("tipo_refeicao == 'Jantar'").valor_total_conta

# Gera o histograma das contas do almoço
sns.distplot(contas_almoco, label="Gráfico do almoço", kde=False, color="Green")
# Gera o histograma das contas do jantar
sns.distplot(contas_jantar, label="Gráfico do jantar", kde=False, color="Black")

plt.show()
