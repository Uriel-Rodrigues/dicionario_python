'''94: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os
dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final,
mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''

dados = dict()
registros = list()
mulheres = list()
acimamedia = list()
cont = 0
media = 0

while True:
    dados['nome'] = str(input('Nome para registro: ')).strip().upper()
    dados['idade'] = int(input('Idade para registro: '))
    dados['sexo'] = str(input('sexo para registro  M/F: ')).strip().upper()

    cont = 1 + cont
    media = media + dados['idade']
    registros.append(dados.copy())
    if dados['sexo'] in 'F':
        mulheres.append(dados['nome'])

    parada = str(input('parar registros SIM/NAO: ')).strip().upper()
    if "SIM" in parada:
        break
for i, v in enumerate(registros):
    if (registros[i]["idade"]) > media/2:
        acimamedia.append(registros[i]["nome"])

print('-='*30)
print(f'{"RESUMO DO REGISTRO":^51}')
print('-='*30)

print(f'- N° REGISTROS: {cont}')
print(f'- MEDIA DE IDADES: {media/2}')

print('-='*30)
print(f'{"MULHESRES REGISTRADAS":^51}')
print('-='*30)
for i, m in enumerate(mulheres):
    print(f'({i+1}) {m}')

print('-='*30)
print(f'{"IDADE ACIMA DA MEDIA":^51}')
print('-='*30)
for i, a in enumerate(acimamedia):
    print(f'({i+1}) {a}')