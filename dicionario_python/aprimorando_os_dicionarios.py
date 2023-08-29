'''95 - Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema
de visualização de detalhes do aproveitamento de cada jogador.'''

jogador = dict()
registros = list()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('digite o nome do jogador: '))
    tot = int(input('digite o numero de partidas: '))

    for p in range(0, tot):
        partidas.append(int(input(f'N° cestas partida {p+1}: ')))
    jogador['cestas'] = partidas[:]
    jogador['total'] = sum(partidas)
    partidas.clear()
    registros.append(jogador.copy())
    while True:
        saida = str(input('gostaria de sair? S/N: ')).strip().upper()
        if saida in 'SN':
            break
        print('ERROR! digitar somente  S (sim) ou N (nao)')
    if saida in 'S':
        break

print('-=' * 30)
print(f'{"LEVANDAMENTO DE DADOS":^60}')
print('-=' * 30)
print('cod ',end='')
for c in jogador.keys():
    print(f'{c:<15}',end='')
print()
print('-=' * 30)
for k, v in enumerate(registros):
    print(f'{k:<4}',end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    buscar = int(input('digie o godigo do jogador para buscar: '))
    if buscar == 999:
        break
    elif buscar >= len(registros):
        print('ERROR! valor nao entcontrado')
    else:
        print('---- LEVANTAMEBNTO DO JOGARDOR ----')
        for i, g in enumerate(registros[buscar]['cestas']):
            print(f' no jogo {i+1} fez {g} cestas')

'''print(registros)
print(partidas)'''