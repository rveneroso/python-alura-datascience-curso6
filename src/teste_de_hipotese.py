import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import ranksums
dados = pd.read_csv('../data/tips_traduzido.csv', sep=';')
sobremesa = dados.query("sobremesa == 'Sim'").porcentagem
nao_sobremesa = dados.query("sobremesa == 'Não'").porcentagem

# Executa o teste de hipótese. Basicamente verifica se há igualdade de distribuição entre dois grupos distintos.
# Hipótese nula: a distribuição da taxa de gorjeta é a mesma nos dois grupos.
# Hipótese alternativa: a distribuição da taxa de gorjeta não é a mesma nos dois grupos.
resultado_hipotese = ranksums(sobremesa, nao_sobremesa)
# O cálculo acima resulta em:
#       RanksumsResult(statistic=-0.6331073145314825, pvalue=0.5266635660124415)
# Nesse caso a hipótese alternativa é rejeitada pois ela é aceita somente nos casos em que o pvalue resulta
# em valores iguais ou menores que 0.05. Como o pvalue resultou em 0.52, somente a hipótese nula é válida.
print(f'O valor do pvalue para esse teste de hipótese  é {resultado_hipotese.pvalue}')

# Obtém a porcentagem da gorjeta dada pelas pessoas que pediram sobremesa.


# Obtém a porcentagem da gorjeta dada pelas pessoas que não pediram sobremesa.

# Segunda hipótese: a distribuição da taxa de gorjeta não é a mesma nos dois grupos.


