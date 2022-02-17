import pandas as pd
dados = pd.read_csv('../data/tips_traduzido.csv', sep=';')

# Exibindo a média geral dos valores de gorjeta
media_geral_gorjetas = dados['valor_gorjeta'].mean()
print(f'O valor médio da gorjeta é {media_geral_gorjetas}')

# Exibindo a média geral dos valores de gorjeta agrupada por dia da semana
media_gorjeta_dia_da_semana = dados.groupby(['dia_da_semana']).mean()
print('Valor médio da gorjeta por dia da semana')
print(media_gorjeta_dia_da_semana)

# Selecionando colunas específicas a serem exibidas na saída
media_gorjeta_dia_da_semana = dados.groupby(['dia_da_semana']).mean()[['valor_total_conta', 'valor_gorjeta', 'porcentagem']]
print('Valor médio da gorjeta por dia da semana')
print(media_gorjeta_dia_da_semana)

# Imprimindo a frequência de contas em cada um dos dias da semana
print('Frequência por dia da semana')
print(dados['dia_da_semana'].value_counts())
