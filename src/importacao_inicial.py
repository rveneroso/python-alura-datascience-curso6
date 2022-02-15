import pandas as pd
pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 100)
dados = pd.read_csv('../data/tips.csv')

# Cria um dicionário com os nomes das colunas inglês / português
renomear = {
    'total_bill' : 'valor_total_conta',
    'tip' : 'valor_gorjeta',
    'dessert' : 'sobremesa',
    'day' : 'dia_da_semana',
    'time' : 'tipo_refeicao',
    'size' : 'quantidade_pessoas'
}

# Cria um novo DataFrame já renomeando as colunas
gorjetas = dados.rename(columns=renomear)

# Para visualizar uma lista distinta de valores existentes em uma coluna de DataFrame
# print(gorjetas.tipo_refeicao.unique())

# Dicionário de tradução dos valores da coluna sobremesa
sim_nao = {
    'No' : 'Não',
    'Yes' : 'Sim'
}
# Realiza a tradução dos valores da coluna sobremesa
gorjetas.sobremesa = gorjetas.sobremesa.map(sim_nao)

# Dicionário de tradução dos dias da semana
dias_semana = {
    'Sun' : 'Dom',
    'Mon' : 'Seg',
    'Tue' : 'Ter',
    'Web' : 'Qua',
    'Thu' : 'Qui',
    'Fri' : 'Sex',
    'Sat' : 'Sab'
}
# Realiza a tradução dos nomes dos dias da semana
gorjetas.dia_da_semana = gorjetas.dia_da_semana.map(dias_semana)

# Dicionário de tradução do tipo de refeição
tipos_refeicao = {
    'Lunch' : 'Almoço',
    'Dinner' : 'Jantar'
}
# Realiza a tradução dos tipos de refeição
gorjetas.tipo_refeicao = gorjetas.tipo_refeicao.map(tipos_refeicao)

# Salva o DataFrame com as traduções em um novo arquivo csv.
gorjetas.to_csv('../data/tips_traduzido.csv', sep=';')
