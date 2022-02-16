import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
dados = pd.read_csv('../data/tips_traduzido.csv', sep=';')

# Gera um gráfico discriminando apenas quem pediu e quem não pediu sobremesa.
#sns.catplot(x='sobremesa', y='valor_gorjeta', data=dados)

# Gera um gráfico descrevendo a relação Valor da Conta X Valor da Gorjeta destacando, em cada ponto,
# quem pediu e quem não pediu sobremesa.
# sns.relplot(x='valor_total_conta', y='valor_gorjeta', hue='sobremesa', data=dados)

# Gera dois gráficos que nada mais são do que a separação do gráfico acima em quem pediu e quem não pediu
# sobremesa.
# sns.relplot(x='valor_total_conta', y='valor_gorjeta', hue='sobremesa', col='sobremesa',data=dados)

# Gera um gráfico com a distribuição entre quem pediu e quem não pediu sobremesa traçando uma reta
# em cada um desses gráficos.
# sns.lmplot(x='valor_total_conta', y='valor_gorjeta', col='sobremesa', hue='sobremesa', data=dados)

# Gera os mesmos gráficos acima porém baseados na porcentagem da gorjeta em relação ao valor total da conta.
# sns.lmplot(x='valor_total_conta', y='porcentagem', col='sobremesa', hue='sobremesa', data=dados)

# Gera gráficos semelhantes aos acima porém com linhas em vez de pontos.
sns.relplot(x='valor_total_conta', y='valor_gorjeta', col='sobremesa', hue='sobremesa', kind='line', data=dados)
plt.show()


