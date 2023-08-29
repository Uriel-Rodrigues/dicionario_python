'''92 - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e
cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO,
o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente,
além da idade, com quantos anos a pessoa vai se aposentar.'''

from datetime import datetime

registro = dict()

for c in range(1):
    registro['nome'] = str(input('Nome para registro: ')).strip()
    registro['anonascimento'] = int(input('ano de nascimento para registro: '))
    registro['idade'] = datetime.now().year - registro['anonascimento']
    registro['carttrab'] = int(input('N° carteira de trabalho para registro (0=SEM CARTEIRA): '))

if registro['carttrab'] != 0:
    registro['anocontrat'] = int(input('ano de contratação para registro: '))
    registro['salario'] = int(input(('salario para registro: ')))
    registro['aposentadoria'] = (datetime.now().year - registro['anonascimento']) + 65



print('------- DADOS REGISTRADOS -------')
print(f'nome: {registro["nome"]}')
print(f'nascimento: {registro["anonascimento"]}')
print(f'idade: {registro["idade"]} anos')
print(f'carteira: {registro["carttrab"]}')

if registro['carttrab'] != 0:
    print(f'contratação: {registro["anocontrat"]}')
    print(f'salario: {registro["salario"]}')
    print(f'aposentadoria com: {registro["aposentadoria"]} anos')

