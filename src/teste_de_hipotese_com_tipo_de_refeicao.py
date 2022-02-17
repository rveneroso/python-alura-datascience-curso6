import pandas as pd
from scipy.stats import ranksums
dados = pd.read_csv('../data/tips_traduzido.csv', sep=';')

medias_por_tipo_refeicao = dados.groupby(['tipo_refeicao']).mean()[['valor_total_conta','valor_gorjeta','porcentagem']]
almoco = dados.query("tipo_refeicao == 'Almoço'").valor_total_conta
jantar = dados.query("tipo_refeicao == 'Jantar'").valor_total_conta
# Hipótese nula: a distribuição do valor da conta é igual no jantar e no almoço.
# Hipótese alternativa: a distribuição do valor da conta não é igual no jantar e no almoço.
resultado_hipotese = ranksums(almoco, jantar)
print(f'O valor do pvalue para esse teste de hipótese  é {resultado_hipotese.pvalue}')
# Nesse caso a hipótese alternativa é aceita pois o pvalue resultou em 0.001, somente a hipótese nula é válida.

porcentagem_almoco = dados.query("tipo_refeicao == 'Almoço'").porcentagem
porcentagem_jantar = dados.query("tipo_refeicao == 'Jantar'").porcentagem
resultado_hipotese = ranksums(porcentagem_almoco, porcentagem_jantar)
print(f'O valor do pvalue para esse teste de hipótese  é {resultado_hipotese.pvalue}')
# Como o p-value é 0.26 então rejeitamentos a hipótese alternativa.
