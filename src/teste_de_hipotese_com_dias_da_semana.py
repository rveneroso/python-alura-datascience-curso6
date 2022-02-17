import pandas as pd
from scipy.stats import ranksums
dados = pd.read_csv('../data/tips_traduzido.csv', sep=';')

# Hipótese nula: a distribuição do valor da conta é igual no sábado e no domingo.
# Hipótese alternativa: a distribuição do valor da conta não é igual no sábado e no domingo.

# Nesse caso a hipótese alternativa é rejeitada pois ela é aceita somente nos casos em que o pvalue resulta
# em valores iguais ou menores que 0.05. Como o pvalue resultou em 0.35, somente a hipótese nula é válida.
valores_do_sabado = dados.query("dia_da_semana == 'Sab'").valor_total_conta
valores_do_domingo = dados.query("dia_da_semana == 'Dom'").valor_total_conta
resultado_hipotese = ranksums(valores_do_domingo, valores_do_sabado)
print(f'O valor do pvalue para esse teste de hipótese  é {resultado_hipotese.pvalue}')