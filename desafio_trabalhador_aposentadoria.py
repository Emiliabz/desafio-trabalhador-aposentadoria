"""
ENUNCIADO:
Crie um programa que leia nome, ano de nascimento e carteira de trabalho
e cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for
diferente de ZERO, o dicionário receberá também o ano de contratação
e o salário. Calcule e acrescente, além da idade, com quantos anos
a pessoa vai se aposentar.
"""
from datetime import datetime

dados = dict()
ano_atual = datetime.now().year

dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = ano_atual - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

if dados['ctps'] != 0:
 dados['contratação'] = int(input('Ano de Contratação: '))
 dados['salário'] = float(input('Salário: R$ '))

 tempo_contribuicao = 35
 anos_trabalhados = ano_atual - dados['contratação']
 dados['aposentadoria'] = dados['idade'] + (tempo_contribuicao - anos_trabalhados)

print('-=' * 30)

for k, v in dados.items():
 print(f' - {k} tem o valor {v}')